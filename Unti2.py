import requests


r = requests.get("https://vk.com")
print(r.status_code)
print("Тут изменения")
print("И тут есть я")
