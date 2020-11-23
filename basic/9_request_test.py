import requests

payload = {"firstName": "matheus", "lastname": "Smith"}
r = requests.post("https://httpbin.org/post", data=payload)
print(r.text)

print("============================================================\n")

payload = {"firstName": "matheus", "lastname": "Smith"}
r = requests.get("https://httpbin.org/get", params=payload)
print(r.text)