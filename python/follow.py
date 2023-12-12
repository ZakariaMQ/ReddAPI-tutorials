import requests

from creds import *

url = "https://reddapi.p.rapidapi.com/api/follow"

payload = {
	"useragent": useragent,  # your useragent
	"proxy": proxy,          # your proxy it should on the following format http://ip:port
	"bearer": bearer,        # for make the auth to reddit bearer is the token_v2 returned from the login endpoint
	"username": username     # of the account you wanna follow
}

headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": X_RapidAPI_Key,   # Get your API key at https://rapidapi.com/SeasonedCode/api/reddapi
	"X-RapidAPI-Host": "reddapi.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())