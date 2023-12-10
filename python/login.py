import requests

from creds import *

url = "https://reddapi.p.rapidapi.com/api/login"

payload = {
	"username": username,
	"password": password,
	"useragent": useragent,
	"proxy": proxy
}

headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": X_RapidAPI_Key,
	"X-RapidAPI-Host": "reddapi.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)