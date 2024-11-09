# Task 1: Define User Model: First, ensure we have Flask and SQLAlchemy installed. We can add these to your requirements.txt file:
# Flask==2.x.x
# Flask-SQLAlchemy==3.x.x
# bcrypt==3.x.x  # For password hashing


# And then create the models.py file:

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    
    def hash_password(self, password):
        self.password = bcrypt.generate_password_hash(password).decode('utf8')
    
    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)