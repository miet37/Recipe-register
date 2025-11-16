from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from model import db
from recipe_blueprint import recipe_bp
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///att_register.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db.init_app(app)
bootstrap = Bootstrap(app)

# Register blueprints
app.register_blueprint(recipe_bp)


@app.route('/')
def index():
    """Render the main landing page."""
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Recipe Register Application</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.0/font/bootstrap-icons.css" rel="stylesheet">
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .main-container {
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            padding: 60px;
            max-width: 600px;
            text-align: center;
        }
        .app-title {
            font-size: 48px;
            font-weight: bold;
            color: #28a745;
            margin-bottom: 20px;
        }
        .app-icon {
            font-size: 80px;
            color: #28a745;
            margin-bottom: 30px;
        }
        .description {
            font-size: 18px;
            color: #6c757d;
            margin-bottom: 40px;
        }
        .btn-launch {
            font-size: 20px;
            padding: 15px 40px;
            border-radius: 50px;
            text-decoration: none;
            transition: all 0.3s;
        }
        .btn-launch:hover {
            transform: translateY(-3px);
            box-shadow: 0 10px 20px rgba(40, 167, 69, 0.3);
        }
    </style>
</head>
<body>
    <div class="main-container">
        <div class="app-icon">
            <i class="bi bi-book"></i>
        </div>
        <div class="app-title">Recipe Register</div>
        <div class="description">
            Organize your favorite recipes by category with an intuitive interface for adding, editing, and managing your culinary collection.
        </div>
        <a href="/recipe/" class="btn btn-success btn-launch btn-lg">
            <i class="bi bi-arrow-right-circle"></i> Launch Recipe Register
        </a>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
    '''


def init_db():
    """Initialize the database with tables."""
    with app.app_context():
        db.create_all()


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
