# 3. `models/user_model.py`: Database Model

## Purpose:
Defines the `User` class, which maps to the `users` table in the PostgreSQL database.

## Key Components:
### `class User(db.Model)`:
- Represents the database table.
- **`__tablename__ = 'users'`**: Specifies the table name.
- Column definitions:
  - `id`, `first_name`, `last_name`, `email`, `mobile_no`, `alternate_mobile_no`, `address_1`, `address_2`, `address_3`, `bank_name`, `bank_acc_no`, `ifsc_code`, `branch_name`, `broker_name`, `broker_acc_no`, `login_id`, `password`, `server_name`, `amount_deposited`:  
    Column definitions with data types, constraints, and attributes.

### `__init__()`:
- Constructor to initialize a new `User` object.

## Key Attributes:
- Each attribute corresponds to a column in the `users` table.

## Dependencies:
- `flask_sqlalchemy`
- `app.db`
- `sqlalchemy`
