"""
Flask Application Entry Point
================================
This script initializes and runs the Flask application.

Application Structure:
  - app/__init__.py: Application factory (create_app function)
  - app/routes/: Route blueprints (auth, product, user)
  - app/controllers/: Business logic handlers
  - app/models/: Database models
  - app/templates/: Jinja2 HTML templates
  - config.py: Configuration (database, secret key, etc.)
"""

from app import create_app

app = create_app()

if __name__ == "__main__":
    # Run the development server
    # Access at http://localhost:5000
    app.run(debug=True, host="0.0.0.0", port=5000)