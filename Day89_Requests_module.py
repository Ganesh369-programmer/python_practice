import requests

response = requests.get('https://www.google.com')
print(response.text)

url = "https://api.example.com/login"
headers = {
    "username" : "myusername",
    "password" : "mypassword"
}

res = requests.post(url , headers=headers )
print(response.text)

