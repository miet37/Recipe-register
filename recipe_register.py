from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from flask_bootstrap import Bootstrap5
import sqlite3
import os
from datetime import datetime

app = Flask(__name__)
app.config['DATABASE'] = 'recipes.db'
app.config['SECRET_KEY'] = 'your-secret-key-here-change-in-production'
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
bootstrap = Bootstrap5(app)

def get_db():
    """Create a database connection."""
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initialize the database with tables."""
    conn = get_db()
    cursor = conn.cursor()
    
    # Create recipes table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS recipes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            ingredients TEXT NOT NULL,
            processing TEXT NOT NULL,
            tips TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()

@app.route('/')
def index():
    """Render the main page with recipes list."""
    category = request.args.get('category', '')
    search = request.args.get('search', '')
    
    conn = get_db()
    cursor = conn.cursor()
    
    # Get all categories
    cursor.execute('SELECT DISTINCT category FROM recipes ORDER BY category')
    categories = [row['category'] for row in cursor.fetchall()]
    
    # Build query based on filters
    query = 'SELECT * FROM recipes WHERE 1=1'
    params = []
    
    if category:
        query += ' AND category = ?'
        params.append(category)
    
    if search:
        query += ' AND (name LIKE ? OR category LIKE ? OR ingredients LIKE ? OR processing LIKE ? OR tips LIKE ?)'
        search_param = f'%{search}%'
        params.extend([search_param] * 5)
    
    query += ' ORDER BY updated_at DESC, created_at DESC'
    
    cursor.execute(query, params)
    recipes = [dict(row) for row in cursor.fetchall()]
    
    conn.close()
    
    return render_template('index.html', 
                         recipes=recipes, 
                         categories=categories,
                         current_category=category,
                         current_search=search,
                         year=datetime.now().year)

@app.route('/recipe/new')
def new_recipe():
    """Render the form to add a new recipe."""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT DISTINCT category FROM recipes ORDER BY category')
    categories = [row['category'] for row in cursor.fetchall()]
    conn.close()
    
    return render_template('recipe.html', recipe=None, categories=categories, year=datetime.now().year)

@app.route('/recipe/<int:recipe_id>')
def edit_recipe(recipe_id):
    """Render the form to edit an existing recipe."""
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM recipes WHERE id = ?', (recipe_id,))
    recipe = cursor.fetchone()
    
    cursor.execute('SELECT DISTINCT category FROM recipes ORDER BY category')
    categories = [row['category'] for row in cursor.fetchall()]
    
    conn.close()
    
    if recipe:
        return render_template('recipe.html', recipe=dict(recipe), categories=categories, year=datetime.now().year)
    
    flash('Recipe not found', 'error')
    return redirect(url_for('index'))

@app.route('/recipe/save', methods=['POST'])
def save_recipe():
    """Save a new or updated recipe."""
    recipe_id = request.form.get('id')
    name = request.form.get('name')
    category = request.form.get('category')
    ingredients = request.form.get('ingredients')
    processing = request.form.get('processing')
    tips = request.form.get('tips', '')
    
    conn = get_db()
    cursor = conn.cursor()
    
    if recipe_id:
        # Update existing recipe
        cursor.execute('''
            UPDATE recipes 
            SET name = ?, category = ?, ingredients = ?, processing = ?, tips = ?,
                updated_at = CURRENT_TIMESTAMP
            WHERE id = ?
        ''', (name, category, ingredients, processing, tips, recipe_id))
        flash('Recipe updated successfully!', 'success')
    else:
        # Create new recipe
        cursor.execute('''
            INSERT INTO recipes (name, category, ingredients, processing, tips)
            VALUES (?, ?, ?, ?, ?)
        ''', (name, category, ingredients, processing, tips))
        flash('Recipe added successfully!', 'success')
    
    conn.commit()
    conn.close()
    
    return redirect(url_for('index'))

@app.route('/recipe/delete/<int:recipe_id>', methods=['POST'])
def delete_recipe(recipe_id):
    """Delete a recipe."""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM recipes WHERE id = ?', (recipe_id,))
    conn.commit()
    conn.close()
    
    flash('Recipe deleted successfully!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run()
