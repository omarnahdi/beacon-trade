import requests
import json

# Testing the /login request with JWT authentication

url = "http://127.0.0.1:5000/login" # make sure the url matches with what is running
headers = {'Content-Type': 'application/json'}
payload = {
    "email": "test@gmail.com",  # Replace with your valid email
    "password": "test"      # Replace with your valid password
}

try:
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
    print("Response status code:", response.status_code)
    print("Response JSON:", response.json())
except requests.exceptions.RequestException as e:
    print("Error making request:", e)