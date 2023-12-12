import requests

from creds import *

url = "https://reddapi.p.rapidapi.com/api/user_info"

querystring = {            # these are the queries needed 2 are required username and proxy rest are optional
    "username":"reddit",   # for more info see http://reddapi.online/docs#user-info
    "proxy":"ip:port",
    "total_karma":"true",
    "post_karma":"true",
    "comments_karma":"true",
    "accept_chats":"false",
    "accept_pms":"false",
    "is_banned":"true",
    "is_not_reported":"true"
    }


headers = {
	"X-RapidAPI-Key": X_RapidAPI_Key,   # Get your API key at https://rapidapi.com/SeasonedCode/api/reddapi
	"X-RapidAPI-Host": "reddapi.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())