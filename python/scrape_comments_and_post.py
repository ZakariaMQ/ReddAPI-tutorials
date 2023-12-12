import requests

from creds import *

url = "https://reddapi.p.rapidapi.com/api/scrape_new_comments_and_its_post_content"

querystring = {
    "proxy":"ip:port",                 # these are the queries needed 2 are required post_url and proxy
    "post_url":"the url of the post",  # 1 optional comments_num default: 15
    "comments_num":"5"                 # for more info see http://reddapi.online/docs#scrape-new-comments
    }

headers = {
	"X-RapidAPI-Key": X_RapidAPI_Key,   # Get your API key at https://rapidapi.com/SeasonedCode/api/reddapi
	"X-RapidAPI-Host": "reddapi.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())