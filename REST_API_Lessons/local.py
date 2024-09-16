import requests

resp = requests.post("http://127.0.0.1:3000/api/courses/3", json={"name": "Golang", "videos": 5})
resp = requests.post("http://127.0.0.1:3000/api/courses/4", json={"name": "PHP", "videos": 15})

print(resp.json())
