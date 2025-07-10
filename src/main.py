import requests

def get_ip():
    res = requests.get("https://api.ipify.org?format=json")
    return res.json()["ip"]