from flask import flash, redirect, render_template, request, url_for


class AuthController:
    def login(self):
        if request.method == "POST":
            flash("Login submitted - no backend database.", "info")
        return render_template("login.html")

    def register(self):
        if request.method == "POST":
            flash("Registration submitted - no backend database.", "info")
        return render_template("register.html")

    def forgot_password(self):
        if request.method == "POST":
            flash("Password reset submitted - no backend database.", "info")
        return render_template("forgot_password.html")

    def logout(self):
        flash("Logged out - no backend database.", "info")
        return redirect(url_for("auth.home"))
