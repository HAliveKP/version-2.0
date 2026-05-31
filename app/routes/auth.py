from flask import Blueprint
from app.controllers.auth import AuthController
from app.auth import login_required, admin_required

class AuthRoutes:
    def __init__(self):
        self.bp = Blueprint("auth", __name__)
        self.controller = AuthController()

    def register(self):
        """Register all authentication-related routes."""
        self.bp.route("/login", methods=["GET", "POST"])(
            self.controller.login
        )
        self.bp.route("/register", methods=["GET", "POST"])(
            self.controller.register
        )
        self.bp.route("", methods=["GET", "POST"])(
            self.controller.home
        )
        self.bp.route("/dashboard", methods=["GET", "POST"])(
            login_required(self.controller.dashboard)
        )
        self.bp.route("/logout", methods=["GET"])(
            login_required(self.controller.logout)
        )

        
        return self.bp