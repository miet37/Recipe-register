# Usage Guide

## Quick Start

1. Start the application:
```bash
python app.py
```

2. Open your browser and go to: `http://localhost:5000`

## Using the Recipe Register

### Adding a Recipe

1. Click the **"Add"** button in the top right corner
2. Fill in the recipe form:
   - **Recipe Name**: Give your recipe a descriptive name
   - **Category**: Enter a category (e.g., Breakfast, Lunch, Dinner, Dessert)
   - **Ingredients**: List all ingredients, one per line
   - **Processing/Instructions**: Describe the cooking steps
   - **Tips** (optional): Add any helpful cooking tips
3. Click **"Save Recipe"** to save

### Viewing Recipes

- **All Recipes**: Click "All Recipes" in the left panel to see all recipes
- **By Category**: Click any category in the left panel to filter recipes
- **Recipe Details**: Click on any recipe in the middle panel to view full details

### Editing a Recipe

1. Select the recipe you want to edit by clicking on it
2. Click the **"Edit"** button in the top right
3. Modify the recipe fields
4. Click **"Save Recipe"** to save changes

### Deleting a Recipe

1. Select the recipe you want to delete by clicking on it
2. Click the **"Delete"** button in the top right
3. Confirm the deletion

## Tips

- **Categories**: Categories are automatically created when you add recipes
- **Organization**: Use consistent category names for better organization
- **Search**: Filter by category to quickly find recipes
- **Ingredients**: Format ingredients clearly, one per line for readability
- **Instructions**: Number your steps for easy following

## Example Categories

- Breakfast
- Lunch
- Dinner
- Dessert
- Appetizer
- Snack
- Beverage
- Salad
- Soup
- Main Course
- Side Dish
- Baking

## Database

All recipes are stored in a SQLite database file called `recipes.db` in the application directory. This file is automatically created when you first run the application.

## Troubleshooting

### Port Already in Use

If port 5000 is already in use, you can modify the port in `app.py`:
```python
if __name__ == '__main__':
    init_db()
    app.run(port=5001)  # Change to any available port
```

### Database Issues

If you need to reset the database:
1. Stop the application
2. Delete the `recipes.db` file
3. Restart the application (it will create a new database)

### Browser Issues

If the page doesn't load properly:
1. Try clearing your browser cache
2. Make sure JavaScript is enabled
3. Try a different browser (Chrome, Firefox, Safari, Edge)
