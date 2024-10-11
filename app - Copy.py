# app.py
# Ver 2024.10.10
# For SlamSim

from flask import Flask, request
from flask_wtf import CSRFProtect  

# SQLite Database Setup
from flask_sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__)

    # Configurations should be inside the create_app function
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///slamsim.db'

    # Configure the upload folder
    app.config['UPLOAD_FOLDER'] = 'uploads/'
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB limit
    app.config['SECRET_KEY'] = 'your_secret_key'

    # Initialize extensions
    db = SQLAlchemy()
    db.init_app(app)

    # Import routes
    from routes.home import home_routes
    from routes.leagues import league_routes

    # Register blueprints
    app.register_blueprint(home_routes)
    app.register_blueprint(league_routes)

    return app  # Make sure to return the app

# Ensure the app runs if the script is executed directly
if __name__ == '__main__':
    app = create_app()  # Call the function to create the app
    app.run(debug=True)
