

data_test = {
    "full_name": "John Doe",
    "email": "john@example.com",
    "action_type": "vacancy"
}

import requests

enpoint = 'http://127.0.0.1:8000/submit-contact/'

contact_response = requests.post(enpoint, json=data_test)
print(contact_response.status_code)