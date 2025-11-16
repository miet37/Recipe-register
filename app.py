from flask import Flask, render_template, request, jsonify
import sqlite3
import os

app = Flask(__name__)
app.config['DATABASE'] = 'recipes.db'

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
            tips TEXT
        )
    ''')
    
    conn.commit()
    conn.close()

@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')

@app.route('/api/categories', methods=['GET'])
def get_categories():
    """Get all unique categories."""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT DISTINCT category FROM recipes ORDER BY category')
    categories = [row['category'] for row in cursor.fetchall()]
    conn.close()
    return jsonify(categories)

@app.route('/api/recipes', methods=['GET'])
def get_recipes():
    """Get all recipes or filter by category."""
    category = request.args.get('category')
    conn = get_db()
    cursor = conn.cursor()
    
    if category:
        cursor.execute('SELECT * FROM recipes WHERE category = ? ORDER BY name', (category,))
    else:
        cursor.execute('SELECT * FROM recipes ORDER BY name')
    
    recipes = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return jsonify(recipes)

@app.route('/api/recipes/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    """Get a specific recipe by ID."""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM recipes WHERE id = ?', (recipe_id,))
    recipe = cursor.fetchone()
    conn.close()
    
    if recipe:
        return jsonify(dict(recipe))
    return jsonify({'error': 'Recipe not found'}), 404

@app.route('/api/recipes', methods=['POST'])
def create_recipe():
    """Create a new recipe."""
    data = request.json
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO recipes (name, category, ingredients, processing, tips)
        VALUES (?, ?, ?, ?, ?)
    ''', (data['name'], data['category'], data['ingredients'], 
          data['processing'], data.get('tips', '')))
    
    conn.commit()
    recipe_id = cursor.lastrowid
    conn.close()
    
    return jsonify({'id': recipe_id, 'message': 'Recipe created successfully'}), 201

@app.route('/api/recipes/<int:recipe_id>', methods=['PUT'])
def update_recipe(recipe_id):
    """Update an existing recipe."""
    data = request.json
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute('''
        UPDATE recipes 
        SET name = ?, category = ?, ingredients = ?, processing = ?, tips = ?
        WHERE id = ?
    ''', (data['name'], data['category'], data['ingredients'], 
          data['processing'], data.get('tips', ''), recipe_id))
    
    conn.commit()
    conn.close()
    
    return jsonify({'message': 'Recipe updated successfully'})

@app.route('/api/recipes/<int:recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
    """Delete a recipe."""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM recipes WHERE id = ?', (recipe_id,))
    conn.commit()
    conn.close()
    
    return jsonify({'message': 'Recipe deleted successfully'})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
