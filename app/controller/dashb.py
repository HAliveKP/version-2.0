from flask import render_template


class DashboardController:
    def index(self):
        stats = [
            {"label": "Active projects", "value": "08", "detail": "Two launches are moving this week."},
            {"label": "Open tasks", "value": "24", "detail": "Five tasks need follow-up before Friday."},
            {"label": "Team health", "value": "92%", "detail": "Momentum is strong across delivery pods."},
            {"label": "Client updates", "value": "06", "detail": "Status notes ready for review and send."},
        ]

        projects = [
            {"name": "Website refresh", "status": "On track", "progress": 76, "lead": "Rina Shrestha", "due_date": "May 28"},
            {"name": "Operations dashboard", "status": "Needs input", "progress": 54, "lead": "Sajan Karki", "due_date": "June 03"},
            {"name": "Onboarding journey", "status": "Planning", "progress": 31, "lead": "Mina Gurung", "due_date": "June 12"},
        ]

        activity = [
            "A sprint summary is ready for your afternoon check-in.",
            "Two new collaborators joined the delivery workspace.",
            "The design review packet was updated 15 minutes ago.",
        ]

        return render_template(
            "dashboard/index.html",
            user={"full_name": "Demo User", "username": "demouser", "email": "demo@bhetam.local"},
            user_initials="DU",
            stats=stats,
            projects=projects,
            activity=activity,
        )
