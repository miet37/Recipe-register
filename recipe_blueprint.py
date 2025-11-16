from flask import Blueprint, render_template, request, jsonify
from model import db, Recipe

recipe_bp = Blueprint('recipe', __name__, url_prefix='/recipe')


@recipe_bp.route('/')
def index():
    """Render the recipe register page."""
    return render_template('recipe_index.html')


@recipe_bp.route('/api/categories', methods=['GET'])
def get_categories():
    """Get all unique categories."""
    categories = db.session.query(Recipe.category).distinct().order_by(Recipe.category).all()
    return jsonify([cat[0] for cat in categories])


@recipe_bp.route('/api/recipes', methods=['GET'])
def get_recipes():
    """Get all recipes or filter by category."""
    category = request.args.get('category')
    
    if category:
        recipes = Recipe.query.filter_by(category=category).order_by(Recipe.name).all()
    else:
        recipes = Recipe.query.order_by(Recipe.name).all()
    
    return jsonify([recipe.to_dict() for recipe in recipes])


@recipe_bp.route('/api/recipes/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    """Get a specific recipe by ID."""
    recipe = Recipe.query.get(recipe_id)
    
    if recipe:
        return jsonify(recipe.to_dict())
    return jsonify({'error': 'Recipe not found'}), 404


@recipe_bp.route('/api/recipes', methods=['POST'])
def create_recipe():
    """Create a new recipe."""
    data = request.json
    
    recipe = Recipe(
        name=data['name'],
        category=data['category'],
        ingredients=data['ingredients'],
        processing=data['processing'],
        tips=data.get('tips', '')
    )
    
    db.session.add(recipe)
    db.session.commit()
    
    return jsonify({'id': recipe.id, 'message': 'Recipe created successfully'}), 201


@recipe_bp.route('/api/recipes/<int:recipe_id>', methods=['PUT'])
def update_recipe(recipe_id):
    """Update an existing recipe."""
    recipe = Recipe.query.get_or_404(recipe_id)
    data = request.json
    
    recipe.name = data['name']
    recipe.category = data['category']
    recipe.ingredients = data['ingredients']
    recipe.processing = data['processing']
    recipe.tips = data.get('tips', '')
    
    db.session.commit()
    
    return jsonify({'message': 'Recipe updated successfully'})


@recipe_bp.route('/api/recipes/<int:recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
    """Delete a recipe."""
    recipe = Recipe.query.get_or_404(recipe_id)
    db.session.delete(recipe)
    db.session.commit()
    
    return jsonify({'message': 'Recipe deleted successfully'})
