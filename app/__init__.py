from flask import Flask
import os
import secrets
from datetime import timedelta

def create_app():
    """Initialize the core application"""
    app = Flask(__name__, instance_relative_config=False)
    
    # Generate a secure secret key
    app.secret_key = secrets.token_hex(16)
    app.permanent_session_lifetime = timedelta(days=7)
    
    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    with app.app_context():
        # Import parts of our application
        from app.routes import auth, main
        
        # Register blueprints
        app.register_blueprint(auth.auth_bp)
        app.register_blueprint(main.main_bp)
        
        return app 