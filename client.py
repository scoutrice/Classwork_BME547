import requests 

r = requests.get("http://127.0.0.1:500/info")
print(r.status_code)
print(r.text)

