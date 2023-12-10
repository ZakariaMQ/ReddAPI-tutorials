import requests

from creds import *

url = "https://reddapi.p.rapidapi.com/api/cross_post"


payload = {
	"useragent": useragent,  # your useragent
	"proxy": proxy,          # your proxy it should on the following format http://ip:port
	"bearer": bearer,        # for make the auth to reddit bearer is the token_v2 returned from the login endpoint
	"title": title,          # the post title
	"text": text,            # the post body
    "sub_reddit": subreddit, # the name of the subreddit you wanna post in
    "post_url": post_url,    # the url of the post you wanna cross post
	"is_nsfw": "either true or false" # true if it is nsfw false if it isn't nsfw
}

headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": X_RapidAPI_Key,   # Get your API key at https://rapidapi.com/SeasonedCode/api/reddapi
	"X-RapidAPI-Host": "reddapi.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())