import requests

enpoint = 'http://127.0.0.1:8000/api/v1/vacancies/uxui-designer/'

get_response = requests.get(enpoint)
print(get_response.json())