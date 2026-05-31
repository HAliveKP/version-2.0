from flask import Blueprint
from app.controllers.productctrl import Product
from app.auth import login_required, admin_required

class ProductRoutes:
    """
    Product management routes.
    All product-related operations like viewing, creating, updating, deleting products.
    """
    def __init__(self):
        self.bp = Blueprint("product", __name__)
        self.controller = Product()

    def register(self):
        """Register all product routes."""
        self.bp.route("/all", methods=["GET"])(
            login_required(self.controller.getProduct)
        )

        return self.bp