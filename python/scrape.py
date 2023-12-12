import requests

from creds import *

url = "https://reddapi.p.rapidapi.com/api/scrape"

querystring = {
    "proxy":"ip:port",       # these are the queries needed 2 are required username and proxy
    "subreddit":"askreddit", # 1 optional sort either 'hot' or 'top
    "sort":"hot"             # for more info see http://reddapi.online/docs#scrape
    }

headers = {
	"X-RapidAPI-Key": X_RapidAPI_Key,   # Get your API key at https://rapidapi.com/SeasonedCode/api/reddapi
	"X-RapidAPI-Host": "reddapi.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())