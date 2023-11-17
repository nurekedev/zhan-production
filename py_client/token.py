import requests

enpoint = 'http://127.0.0.1:8000/auth/'

auth_response = requests.post(enpoint, json={'username':'nurekedev', 'password':'123'})

print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {
        'Authorization': f"Token {token}"
    }

    enpoint_2='http://127.0.0.1:8000/api/v1/vacancies/'
    get_response = requests.get(enpoint_2)
    print(get_response.status_code)


get_response = requests.get(enpoint)
print(get_response.json())