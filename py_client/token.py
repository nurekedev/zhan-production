import requests
import json

enpoint = 'http://127.0.0.1:8000/en/submit-contactv2/'  # Corrected variable name

data = {
    'full_name': 'John Doe',
    'phone_number': '+1234567890'
}

headers = {
    'Content-Type': 'application/json',
}

response = requests.post(enpoint, json={
    'full_name': 'John Doe',
    'phone_number': '+1234567890'
}, headers=headers)  
# Process the response
print(response.status_code)
print(response.json())
