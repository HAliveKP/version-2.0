# Application Architecture & Structure

## 📋 Overview
This is a Flask web application with a well-organized MVC (Model-View-Controller) architecture using Blueprints for modular route management.

---

## 🏗️ Directory Structure

```
.
├── run.py                      # Entry point
├── config.py                   # Configuration (DB, secrets, etc.)
├── requirements.txt            # Python dependencies
│
└── app/
    ├── __init__.py            # App factory (create_app, register routes/errors)
    ├── auth.py                # Authentication decorators (login_required, admin_required)
    │
    ├── routes/                # Blueprint route definitions
    │   ├── auth.py           # Routes: /auth/login, /auth/register, /auth/dashboard, /auth/logout
    │   ├── product.py        # Routes: /products/all, /products/get/<id>
    │   └── user.py           # Routes: /users/* (admin management, future use)
    │
    ├── controllers/           # Business logic
    │   ├── auth.py           # AuthController (login, register, logout, dashboard)
    │   ├── base_controller.py # Base class with shared utilities
    │   └── productctrl.py    # ProductController (getProduct)
    │
    ├── models/                # Data models & database
    │   ├── database.py       # Database connection & table creation
    │   ├── base_model.py     # Base model with common DB operations
    │   └── user.py           # User model
    │
    ├── static/                # Static files (CSS, images)
    │   ├── css/
    │   └── images/
    │
    └── templates/             # Jinja2 HTML templates
        ├── base.html          # Base layout (navbar, footer)
        ├── login.html         # Login page
        ├── register.html      # Registration page
        ├── dashboard.html     # Dashboard (admin & user views)
        ├── home.html          # Home page
        ├── about.html         # About page
        ├── contact.html       # Contact page
        ├── notfound.html      # 404 error page
        ├── logout.html        # Logout confirmation
        ├── partials/
        │   └── nav.html       # Navigation partial
        └── product/
            └── getproduct.html # Product listing
```

---

## 🔗 How Everything Connects

### 1. **Application Entry & Initialization**
```
run.py 
  → app.create_app()
    → app/__init__.py (Application Factory)
      ├── Database initialization (create_tables)
      ├── register_routes()
      │   ├── AuthRoutes blueprint → /auth/*
      │   ├── ProductRoutes blueprint → /products/*
      │   └── UserRoutes blueprint → /users/*
      └── register_error_handlers()
          ├── 404 → notfound.html
          └── 500 → notfound.html
```

### 2. **Request Flow (Example: Login)**
```
POST /auth/login (user submits login form)
  ↓
AuthRoutes blueprint (routes/auth.py)
  ↓
AuthController.login() (controllers/auth.py)
  ↓
User.find_by() (models/user.py)
  ↓
Database.fetch_one() (models/database.py)
  ↓
Verify password → Create session
  ↓
Redirect → dashboard
```

### 3. **Route Registration System**
All routes are centralized in `app/__init__.py`:
```python
def register_routes(app):
    auth_routes = AuthRoutes()
    app.register_blueprint(auth_routes.register(), url_prefix='/auth')
    
    product_routes = ProductRoutes()
    app.register_blueprint(product_routes.register(), url_prefix='/products')
    
    user_routes = UserRoutes()
    app.register_blueprint(user_routes.register(), url_prefix='/users')
```

### 4. **Authentication & Authorization**
Decorators in `app/auth.py`:
- `@login_required`: Requires user to be logged in
- `@admin_required`: Requires admin role

Applied to routes:
```python
self.bp.route("/dashboard")(login_required(self.controller.dashboard))
```

---

## 📍 Available Routes

### Authentication Routes (`/auth`)
- `GET/POST /auth/login` → Login page & form
- `GET/POST /auth/register` → Registration page & form
- `GET/POST /auth/` → Home redirect
- `GET/POST /auth/dashboard` → Dashboard (login required)
- `GET /auth/logout` → Logout (login required)

### Product Routes (`/products`)
- `GET /products/all` → Get all products (login required)
- `GET /products/get/<int:id>` → Get specific product (login required)

### User Routes (`/users`)
- Reserved for admin user management (future implementation)

---

## 🔐 Authentication Flow

1. **New User Signup**
   - Register form → AuthController.register()
   - Create User object → User.save()
   - Hash password with werkzeug.security
   - Store in database

2. **User Login**
   - Login form → AuthController.login()
   - Find user by email → User.find_by()
   - Verify password → User.check_password()
   - Create session with user_id, user_name, role
   - Redirect to dashboard

3. **Admin Access**
   - Dashboard checks `session.get('role')`
   - If role == 'admin': Show user management table
   - If role == 'user': Show user profile view
   - Only non-admin users shown in table

4. **Logout**
   - Clear session → session.clear()
   - Redirect to login

---

## 👤 Default Admin Account

- **Email**: `admin@admin.com`
- **Password**: `admin123`
- **Role**: `admin`

Created automatically on first app startup via `Database.create_tables()`

---

## 🗄️ Database Tables

### users table
```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(20) NOT NULL DEFAULT 'user',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
```

---

## 🎯 Key Design Patterns

1. **Application Factory Pattern** (create_app)
   - Centralizes app configuration
   - Enables easy testing and multiple app instances

2. **Blueprint Pattern** (routes)
   - Modular route organization
   - Easy to add new feature modules

3. **MVC Pattern**
   - Routes → Controllers → Models → Database
   - Clear separation of concerns

4. **Decorator Pattern** (auth.py)
   - Route protection with login_required, admin_required
   - Reusable authentication logic

5. **Base Class Pattern** (BaseController, BaseModel)
   - Shared functionality across controllers/models
   - DRY principle

---

## 🔄 Code Flow Examples

### Adding a New Feature
1. Create route in `app/routes/feature.py`
2. Create controller in `app/controllers/featurectrl.py`
3. Register in `app/__init__.py` → register_routes()
4. Create templates in `app/templates/feature/`
5. Define or reuse models in `app/models/`

### Protecting a Route
```python
self.bp.route("/admin-only")(admin_required(self.controller.method))
```

### Accessing Database
```python
user = User()
user_data = user.find_by("email", "user@example.com")
```

---

## 📝 Configuration (`config.py`)

```python
SECRET_KEY = "your-secret-key"
MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = "password"
MYSQL_DB = "database_name"
```

---

## ✅ Current Status

- ✅ Authentication system (login, register, logout)
- ✅ Admin panel with user management
- ✅ Role-based access control
- ✅ Protected routes
- ✅ Error handlers (404, 500)
- ✅ Database initialization
- ✅ Session management
- ✅ Product listing (structure ready)
- ⚠️ User management endpoints (routes defined, controllers needed)
- ⚠️ Product CRUD operations (create, update, delete)

---

## 🚀 Next Steps

1. Implement product CRUD operations
2. Add user management endpoints (admin only)
3. Enhance product listing with filters/search
4. Add profile update feature
5. Implement API endpoints (JSON responses)
6. Add logging system
7. Add form validation
8. Add email notifications
