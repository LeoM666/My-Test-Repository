import requests

print("Helo")
r = requests.get("https://vk.com")
print(r.status_code)
