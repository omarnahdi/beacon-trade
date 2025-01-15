# 2. `config.py`: Configuration Settings

## Purpose:
Stores important configuration variables, such as the database connection string and email settings.

## Key Components:
### `class Config`:
- **`SQLALCHEMY_DATABASE_URI`**: The PostgreSQL database URL.
- **`SQLALCHEMY_TRACK_MODIFICATIONS`**: A SQLAlchemy setting to disable tracking modifications.
- **`EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_USER`, `EMAIL_PASSWORD`, `EMAIL_SENDER`**: Email server settings.
- **`SECRET_KEY`**: A secret key for Flask.

## Key Variables:
- Variables defined within the `Config` class are accessed using `app.config.get('VARIABLE_NAME')` in the application.

## Dependencies:
- `os`
