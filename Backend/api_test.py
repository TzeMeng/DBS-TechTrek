import requests

BASE = "http://127.0.0.1:5000/"

# response = requests.patch(BASE + "expense/2", {})
response = requests.get(BASE + "expense/2", {})
print(response.json())