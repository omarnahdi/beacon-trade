
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env

import os

class Config:
    # Database Configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') # DO NOT add ?sslmode=require in here.
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Database SSL Configuration:
    # If your database requires SSL verification.
    SQLALCHEMY_ENGINE_OPTIONS = {
      'connect_args': {
          "sslmode": "verify-full",
          "sslrootcert": "cacert-2024-12-31.pem", #add the correct path
      }
   }

    # Email Configuration (replace with your email info)
    EMAIL_HOST = os.environ.get('EMAIL_HOST')
    EMAIL_PORT = int(os.environ.get('EMAIL_PORT'))
    EMAIL_USER = os.environ.get('EMAIL_USER')
    EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
    EMAIL_SENDER = os.environ.get('EMAIL_SENDER')
    SECRET_KEY = os.environ.get('SECRET_KEY')
