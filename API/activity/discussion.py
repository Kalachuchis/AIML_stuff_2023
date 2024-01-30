import requests

# api_url = "https://jsonplaceholder.typicode.com/sample"
todo_data = {"userID": 1, "title": "Kain pepe", "completed": True}
headers = {"Content-Type": "application/json"}

api_url = "https://jsonplaceholder.typicode.com/todos/10"

# response = requests.get(api_url)

response = requests.put(api_url, json=todo_data)
print(f"Status Code: {response.status_code}")
print(f"Data: {response.json()}")
print(f"Reason: {response.reason}")
