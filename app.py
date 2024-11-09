# Setting Up the Flask App

# Finally, set up the main Flask app (app.py):

from flask import Flask
from models import db, bcrypt
from auth import auth_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///factory_management.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
bcrypt.init_app(app)

app.register_blueprint(auth_bp, url_prefix='/auth')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)


# Testing

# To test the setup:

    # Run the Flask application.
    # Create a user in your database using SQLAlchemy shell or other methods.
    # Use a tool like Postman to send a POST request to `http://127.0.0.1:
