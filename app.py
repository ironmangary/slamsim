# app.py

from flask import Flask
from db import init_db, db
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///slamsim.db'
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['UPLOAD_FOLDER'] = 'uploads/'
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB

    init_db(app) 
    migrate = Migrate(app, db)

    # Register blueprints
    from routes.home import home_routes
    from routes.leagues import league_routes
    
    app.register_blueprint(home_routes)
    app.register_blueprint(league_routes)
    
    print(app.url_map)



    return app

# Ensure the app is created and run only if the script is executed directly
if __name__ == '__main__':
    app = create_app()  
    app.run(debug=True)
