from flask import Blueprint
from app.controllers.auth import AuthController
from app.auth import login_required

class AuthRoutes:
    def __init__(self):
        self.bp = Blueprint("auth", __name__)
        self.controller = AuthController()

    def register(self):
        self.bp.route("/login", methods=["GET", "POST"])(
            self.controller.login
        )
        self.bp.route("/register", methods=["GET", "POST"])(
            self.controller.register
        )
        self.bp.route("/dashboard", methods = ["GET","POST"])(
            login_required(self.controller.dashboard)
        )
        self.bp.route("/logout", methods = ["GET", "POST"])(
            self.controller.logout
        )
        return self.bp
    
    
        

