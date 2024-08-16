import requests

from creds import *

url = "https://reddapi.p.rapidapi.com/api/post_to_subreddit/image"

payload = {
    "proxy": proxy,          # your proxy it should on the following format http://ip:port or http://user:pass@ip:port
	"cookies": [cookies],    # list of cookies obtained from our login endpoint for authentication
	"title": title,          # the post title
	"subreddit": subreddit,  # subreddit name you want to post to
	"base64_images": ["base64 encoded image1", "base64 encoded image2"], # a list of image(s) encoded into base64
	"is_nsfw": "either true or false" # true if it is nsfw false if it isn't nsfw
}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": X_RapidAPI_Key,  # Get your API key at https://rapidapi.com/SeasonedCode/api/reddapi
	"X-RapidAPI-Host": "reddapi.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())