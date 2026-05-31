from flask import Blueprint
from app.controllers.auth import AuthController
from app.auth import login_required, admin_required

class UserRoutes:
    """
    User management routes.
    Admin-only routes for managing user accounts.
    """
    def __init__(self):
        self.bp = Blueprint("users", __name__)
        self.controller = AuthController()

    def register(self):
        """Register all user management routes."""
        # Future admin routes for user management
        # self.bp.route("", methods=["GET"])(
        #     admin_required(self.controller.get_all_users)
        # )
        # self.bp.route("/<int:user_id>", methods=["GET"])(
        #     admin_required(self.controller.get_user)
        # )
        # self.bp.route("/<int:user_id>", methods=["PUT"])(
        #     admin_required(self.controller.update_user)
        # )
        # self.bp.route("/<int:user_id>", methods=["DELETE"])(
        #     admin_required(self.controller.delete_user)
        # )
        return self.bp