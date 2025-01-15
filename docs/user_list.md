# 6. `templates/user_list.html`: User List Display

## Purpose:
Displays a table of registered users.

## Key Components:
- **HTML table**:
  - Displays user data.
  - Iterates through a list of users (`users`) passed from the Flask route.
- Includes functionality for displaying flashed messages.
- Provides links to the edit page for each user.

## Key Attributes:
- Each table row corresponds to a user in the database.

## Dependencies:
- **Tailwind CSS CDN**
- `static/style.css`
