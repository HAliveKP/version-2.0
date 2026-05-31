from flask import Flask, render_template
from app.routes.auth import AuthRoutes
from app.routes.product import ProductRoutes
from app.routes.user import UserRoutes
from app.models.database import Database
import config

def create_app():
    """
    Application Factory Pattern - Creates and configures the Flask app.
    Centralizes all app setup including:
      - Config loading
      - Database initialization
      - Route registration
      - Error handlers
    """
    app = Flask(__name__)
    app.secret_key = config.SECRET_KEY
    app.config['DEBUG'] = True
    
    # Initialize Database
    with app.app_context():
        Database.create_tables()
    
    # Register all route blueprints
    register_routes(app)
    
    # Register error handlers
    register_error_handlers(app)
    
    return app


def register_routes(app):
    """
    Centralized route registration.
    All routes are registered here in one place for easy management.
    """
    # Auth Routes (login, register, logout, dashboard)
    auth_routes = AuthRoutes()
    app.register_blueprint(auth_routes.register(), url_prefix='/auth')
    
    # Product Routes
    product_routes = ProductRoutes()
    app.register_blueprint(product_routes.register(), url_prefix='/products')
    
    # User Routes (kept separate from auth)
    user_routes = UserRoutes()
    app.register_blueprint(user_routes.register(), url_prefix='/users')


def register_error_handlers(app):
    """
    Centralized error handler registration.
    Handles 404, 500, and other HTTP errors gracefully.
    """
    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('notfound.html'), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return render_template('notfound.html', error="Internal Server Error"), 500

