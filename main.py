import requests
import os
from dotenv import load_dotenv
import sys
load_dotenv()

url = sys.argv[1] if len(sys.argv) > 1 else input("Enter the URL: ")
token = os.getenv("TOKEN")
group_guid = os.getenv("GROUP_GUID")

headers = {
    'Authorization': 'Bearer ' + token,
    'Content-Type': 'application/json',
}

data = f'{{"long_url": "{url}", "domain": "bit.ly", "group_guid": "{group_guid}"}}'

response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, data=data)

print(response.json().get('link'))