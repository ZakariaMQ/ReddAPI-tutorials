import requests

from creds import *

url = "https://reddapi.p.rapidapi.com/api/login"

payload = {
	"username": username,   # your Reddit account username
	"password": password,   # your Reddit account password
	"useragent": useragent, # your useragent
	"proxy": proxy          #your proxy it should on the following format http://ip:port
}

headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": X_RapidAPI_Key,  # Get your API key at https://rapidapi.com/SeasonedCode/api/reddapi
	"X-RapidAPI-Host": "reddapi.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())