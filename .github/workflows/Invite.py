import os
import json
import requests

# Lets go
print("HSMW: Invite")

# Get Secrets
MY_GITHUB_KEY = os.environ['MY_GITHUB_KEY']
COMMUNITY_TEAM_ID = os.environ['COMMUNITY_TEAM_ID']

# Get Data
file = open(os.environ['GITHUB_EVENT_PATH'])
data = json.load(file)
print(f"GitHub-Data:{data}")

# Get Username
USERNAME = data['sender']['login']
print('Invite user @'+USERNAME)

# Send Request
url = 'https://api.github.com/teams/'+COMMUNITY_TEAM_ID+'/memberships/' + USERNAME
payload=''
headers = {
    'Accept': 'application/vnd.github.v3+json',
    'Authorization': 'token '+MY_GITHUB_KEY
}
response = requests.request("PUT", url, headers=headers, data=payload)
print(response.text)
