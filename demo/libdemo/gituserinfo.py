import requests

resp = requests.get("https://api.github.com/users/srikanthpragada")
print(resp.status_code)
details = resp.json()
for name,value in details.items():
    print(f"{name:20} {value}")

