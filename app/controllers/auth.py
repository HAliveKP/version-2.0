
from flask import Flask, render_template, request, redirect,flash, url_for, session
from app.controllers.base_controller import BaseController
from app.modal.user import User

class AuthController(BaseController):

    def __init__(self):
        self.user_model = User()

    def login(self):
        if self.is_logged_in():
            return redirect(url_for("auth.dashboard"))
        if request.method == "POST":
            email, password = self.get_form_data("email", "password")
            password = request.form.get("password", "")
            if not email or not password:
                flash("Email and password are required.", "danger")
                return render_template("login.html")
            user_data = self.user_model.find_by("email", email)
            if user_data:
                user = User.from_db(user_data)
                if user.check_password(password):
                    session["user_id"] = user_data["id"]
                    session["user_name"] = user_data["name"]
                    session["role"] = user_data["role"]
                    return self.flash_and_redirect(
                        "Login successful!", "success", "auth.dashboard"
                    )
            flash("Invalid email or password.", "danger")
        return render_template("login.html")
    
    def home(self):
        #logic to get data

        product = [
            {"name": "mobile", "price": 4000, "manufacture" : 2026},
            {"name": "mobile", "price": 4000, "manufacture" : 2026},
            {"name": "mobile", "price": 4000, "manufacture" : 2026},
            {"name": "mobile", "price": 4000, "manufacture" : 2026},
            {"name": "mobile", "price": 4000, "manufacture" : 2026}
        ]

    def register(self):
        if self.is_logged_in():
            return redirect(url_for("auth.dashboard"))

        if request.method == "POST":
            name, email = self.get_form_data("name", "email")
            password = request.form.get("password", "")

            # Validation
            if not name or not email or not password:
                flash("All fields are required.", "danger")
                return render_template("register.html")

            if len(name) > 100:
                flash("Name must be under 100 characters.", "danger")
                return render_template("register.html")

            if len(password) < 6:
                flash("Password must be at least 6 characters.", "danger")
                return render_template("register.html")

            # Create a new User object and check email
            new_user = User(name=name, email=email, password=password, role="user")

            if new_user.email_exists():
                flash("Email already exists.", "danger")
                return redirect(url_for("auth.register"))

            # Save to database
            new_user.save()
            return self.flash_and_redirect(
                "Registration successful! Please login.", "success", "auth.login"
            )

        return render_template("register.html")
    
    # ------------------------------------------------------------
    def dashboard(self):
        users = self.user_model.find_all_Users()
        print(users)
        return render_template("dashboard.html", users = users)
    
    def logout(self):
        session.clear()
        return self.flash_and_redirect(
            "logged out successfully.", "success", "auth.login"
        )
    
    def editUsers(self, user_id):
        user_data = self.user_model.find_by("id", user_id)
        user_onj = User.from_db(user_data)
        if request.method == "POST":
            name, email = self.get_form_data("name", "email")
            password = request.form.get("password", "")
            
            role = request.form.get("role", "user")

            if not name or not email:
                flash("Name and email are required.", "danger")
                return render_template("edit_user.html", user=user_onj)

            if len(name) > 100:
                flash("Name must be under 100 characters.", "danger")
                return render_template("edit_user.html", user=user_onj)

            if password and len(password) < 6:
                flash("Password must be at least 6 characters.", "danger")
                return render_template("edit_user.html", user=user_onj)

            user_onj.name = name
            user_onj.email = email
            user_onj.role = role

            if password:
                user_onj.password = password

            user_onj.update()
            return self.flash_and_redirect(
                "User updated successfully!", "success", "auth.dashboard"
            )
    
    