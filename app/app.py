"""
Landscape Architecture Film Series (LAFS) Web Application

This Flask application serves as a digital archive and repository of past
installments of LAFS. It preserves and provides access to:

- Historical film series records and documentation
- Past film details and schedule information
- Archive of series data and materials
- Historical venue locations with map visualization

The application is deployed on AWS and can be accessed at https://l-a-f-s.org/.

Architecture:
- Flask web framework with filesystem session storage
- SQLite database with SQLAlchemy ORM
- Google Maps Platform integration
- Modular blueprint structure

Configuration:
- Environment variables for sensitive settings (SECRET_KEY, MAP_API_KEY)
- Development-friendly defaults (template auto-reload, disabled caching)
- File-based session storage for improved security

The application uses blueprints to organize routes and functionality:
- main_bp: Core public-facing routes and views
"""

# Python Standard Library
import os

# Third-Party Libraries
from flask import Flask
from flask_session import Session

# Local
from app.blueprints.main.routes import main_bp










# Configure application
app = Flask(__name__)

# Set secret key for session management
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# Disable file caching and enable template auto-reloading
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

# Initialize session with the app
Session(app)

# Register blueprints for main and cms routes
app.register_blueprint(main_bp)
