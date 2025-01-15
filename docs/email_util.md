# 4. `utils/email_util.py`: Email Utility Functions

## Purpose:
Provides functions for sending emails, such as registration confirmation emails.

## Key Functions:
### `send_registration_email(to_email, account_no, sender_email)`:
- Sends an email to the user with their account number.
- **Steps:**
  - Constructs a MIME message object.
  - Uses `smtplib` to connect to the email server, logs in, and sends the email.

## Key Variables:
- Email server-related variables are retrieved from the `config` file.

## Dependencies:
- `smtplib`
- `email.mime`
- `config.Config`
