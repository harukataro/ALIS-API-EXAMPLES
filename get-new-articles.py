import requests
import json


response = requests.get("https://alis.to/api/articles/recent")
data = json.loads(response.text)

for article in data['Items']:
    url = 'https://alis.to/api/users/' + article['user_id'] + '/info'
    response = requests.get(url) 
    user_name = json.loads(response.text) [ "user_display_name"]
    print(article['title'], user_name)
