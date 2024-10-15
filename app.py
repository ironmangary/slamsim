# app.py
# Ver 2024.10.11
# for SlamSim


import logging
from flask import Flask
from db import init_db, db
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from jinja2 import Environment

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///slamsim.db'
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['UPLOAD_FOLDER'] = 'uploads/'
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB

    init_db(app) 
    migrate = Migrate(app, db)

    # Jinja2 environment
    env = Environment()
    env.filters['safe'] = lambda x: x

    # Enable CSRF protection
    csrf = CSRFProtect(app)
    csrf.init_app(app)
    
        # Register blueprints
    from routes.home import home_routes
    from routes.leagues import league_routes
    
    app.register_blueprint(home_routes)
    app.register_blueprint(league_routes)
    
    # Set up logging
    logging.basicConfig(level=logging.DEBUG)

    return app

# Ensure the app is created and run only if the script is executed directly
if __name__ == '__main__':
    app = create_app()  
    app.run(debug=True)
