# Recipe Register

A simple personal recipe register built with Flask and Bootstrap. This single-page application allows you to organize your recipes by category, with an intuitive interface for adding, editing, and deleting recipes.

## Features

- **Search & Filter**: Search across all recipe fields and filter by category
- **CRUD operations**: Create, Read, Update, and Delete recipes
- **Dedicated recipe page**: Separate page for adding and editing recipes
- **Datetime tracking**: Automatic timestamps for creation and updates
- **SQLite database**: Persistent storage for all recipes
- **Bootstrap styling**: Modern, responsive design using Flask-Bootstrap5
- **Server-side rendering**: No JavaScript required, all logic handled by Flask

## Recipe Information

Each recipe includes:
- Name
- Category
- Ingredients
- Processing/Instructions
- Tips (optional)
- Created timestamp
- Updated timestamp

## Installation

1. Clone the repository:
```bash
git clone https://github.com/miet37/Recipe-register.git
cd Recipe-register
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the application:
```bash
python app.py
```

2. Open your browser and navigate to:
```
http://localhost:5000
```

3. Start adding your recipes!

## How to Use

- **Add Recipe**: Click "Add Recipe" in the navigation menu to create a new recipe
- **Search Recipes**: Use the search box to find recipes by any field (name, ingredients, etc.)
- **Filter by Category**: Select a category from the dropdown to filter recipes
- **View Recipe**: Click the "View" button to see full recipe details in a modal
- **Edit Recipe**: Click the "Edit" button to modify an existing recipe
- **Delete Recipe**: Click the "Delete" button to remove a recipe (with confirmation)

## Technology Stack

- **Backend**: Flask 3.0.0 (Python)
- **Database**: SQLite with datetime tracking
- **Frontend**: HTML, CSS (No JavaScript)
- **Styling**: Flask-Bootstrap5 (bootstrap-flask 2.3.3)
- **Icons**: Unicode emojis

## License

MIT License
