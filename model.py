from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Recipe(db.Model):
    """Recipe model for storing recipe information."""
    __tablename__ = 'recipes'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    processing = db.Column(db.Text, nullable=False)
    tips = db.Column(db.Text)
    
    def to_dict(self):
        """Convert recipe object to dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'ingredients': self.ingredients,
            'processing': self.processing,
            'tips': self.tips or ''
        }
    
    def __repr__(self):
        return f'<Recipe {self.name}>'
