import requests

BASE = "http://127.0.0.1:5000/"
payload = {"Id": 3, "Project_id":3, "Category_id":3, "Name":"TESTn", "Description":"TESTd", "Amount":1, "Created_at": "2020-01-06T00:00:00.000Z", "Created_by":"TESTc", "Updated_at":"2020-01-06T00:00:00.000Z", "Updated_by":"TESTu"}

# response = requests.get(BASE + "expense/1")
response = requests.post(BASE + "expense/3", payload)
# response = requests.patch(BASE + "expense/2", {})
# response = requests.delete(BASE + "expense/2", {})
print(response.json())


