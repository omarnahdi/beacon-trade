# 1. `app.py`: The Main Flask Application

## Purpose:
This file contains the core logic of the Flask web application. It handles routing, database interactions, form processing, and email sending.

## Key Components:
- `app = Flask(__name__)`: Initializes the Flask application.
- `app.config.from_object(Config)`: Loads configuration settings from `config.py`.
- `db = SQLAlchemy(app)`: Initializes the SQLAlchemy database integration.
- `with app.app_context(): db.create_all()`: Creates the database tables.

## Routes:
### 1. `@app.route('/', methods=['GET', 'POST'])`: Handles the user registration form.
- **GET**: Renders the registration form (`register.html`).
- **POST**:
  - Retrieves form data.
  - Hashes the user's password with `generate_password_hash`.
  - Creates a new `User` object using data from the form.
  - Adds the new user to the database.
  - Sends a confirmation email using `send_registration_email` from `email_util.py`.
  - Handles database errors with a rollback.
  - Redirects to the user list page (`user_list.html`) on successful registration.

### 2. `@app.route('/users')`: Handles displaying the user list in tabular format.
- Retrieves all users from the database and renders them in the `user_list.html` page.

### 3. `@app.route('/users/edit/<int:user_id>', methods=['GET', 'POST'])`: Handles editing user details.
- **GET**: Retrieves the user object from the database and renders the `edit_user.html` form.
- **POST**:
  - Retrieves form data.
  - Updates existing user data in the database.
  - Handles database errors with a rollback.
  - Redirects to the user list page (`user_list.html`) on successful update.

### 4. `if __name__ == '__main__': app.run(debug=True)`: Starts the Flask development server when the script is executed directly.

## Key Functions:
- `register()`: Handles user registration logic.
- `list_users()`: Retrieves all users and renders them in tabular form.
- `edit_user(user_id)`: Handles editing the user data.

## Dependencies:
- `Flask`
- `flask_sqlalchemy`
- `werkzeug.security`
- `config.py`
- `models.user_model`
- `utils.email_util`
