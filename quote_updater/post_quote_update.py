import requests
import config

url = config.UDPATE_QUOTE_URL_LOCAL

quote = 'test-quote'
title = 'test-title'
author = 'test-author'

data = {'quote': quote, 'title': title, 'author': author}

# Define any headers needed for authentication (if required)
headers = {'Authorization': 'Bearer YOUR_AUTH_TOKEN'}  # Replace with your authentication token

response = requests.post(url, json=data, headers=headers)

if response.status_code == 200:
    print("API request successful")
    print(response.json())
else:
    print(f"Error {response.status_code}: {response.text}")