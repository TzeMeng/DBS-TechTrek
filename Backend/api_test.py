import requests

BASE = "http://127.0.0.1:5000/"
payload = {"Id": 1, "Project_id":1, "Category_id":1, "Name":"TESTn", "Description":"TESTd", "Amount":1, "Created_by":"TESTc", "Updated_by":"TESTu"}

# response = requests.patch(BASE + "expense/2", {})
response = requests.get(BASE + "expense/1")
print(response.json())