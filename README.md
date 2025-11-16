# Recipe Register

A simple personal recipe register built with Flask and Bootstrap. This single-page application allows you to organize your recipes by category, with an intuitive interface for adding, editing, and deleting recipes.

## Features

- **Three-panel layout**: Categories (2/12), Recipe List (4/12), Recipe Details (6/12)
- **CRUD operations**: Create, Read, Update, and Delete recipes
- **Category organization**: Filter recipes by category
- **Modal popup**: Add/Edit recipes with a clean popup form
- **SQLite database**: Persistent storage for all recipes
- **Bootstrap styling**: Modern, responsive design

## Recipe Information

Each recipe includes:
- Name
- Category
- Ingredients
- Processing/Instructions
- Tips (optional)

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

- **Add Recipe**: Click the "Add" button in the top right to create a new recipe
- **Edit Recipe**: Select a recipe, then click the "Edit" button
- **Delete Recipe**: Select a recipe, then click the "Delete" button
- **Filter by Category**: Click on a category in the left panel to filter recipes
- **View Recipe**: Click on any recipe in the list to see its details

## Technology Stack

- **Backend**: Flask (Python)
- **Database**: SQLite
- **Frontend**: HTML, CSS, JavaScript
- **Styling**: Bootstrap 5
- **Icons**: Bootstrap Icons

## License

MIT License
