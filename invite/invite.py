import os
import json
import requests

# Lets go
print("HSMW: Invite")

# Get Secretspytho
MY_GITHUB_KEY = os.environ['MY_GITHUB_KEY']

# Get Data
file = open(os.environ['GITHUB_EVENT_PATH'])
data = json.load(file)
#print(f"GitHub-Data:{data}")

# Get Username
USERNAME = data['sender']['login']
print('Invite user @'+USERNAME)

# Send Request
url = 'https://api.github.com/orgs/Hochschule-Mittweida/memberships/' + USERNAME
payload=''
headers = {
    'Accept': 'application/vnd.github.v3+json',
    'Authorization': 'token ' + MY_GITHUB_KEY
}
print(f"Request: {url}")
response = requests.request("PUT", url, headers=headers, data=payload)
print(response.text)