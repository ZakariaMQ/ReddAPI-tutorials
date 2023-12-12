import requests

from creds import *

url = "https://reddapi.p.rapidapi.com/api/rising_posts"


querystring = {
    "proxy":"ip:port",       # these are the queries needed 2 are required username and proxy
    "subreddit":"askreddit", # 1 optional post_num either default: 7 posts
    "post_num":"10"          # for more info see http://reddapi.online/docs#rising-posts
    }

headers = {
	"X-RapidAPI-Key": X_RapidAPI_Key,   # Get your API key at https://rapidapi.com/SeasonedCode/api/reddapi
	"X-RapidAPI-Host": "reddapi.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())