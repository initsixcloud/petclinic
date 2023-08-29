import os
import requests

webhook_url = os.environ['WEBHOOK_URL']

pr_title = os.environ['GITHUB_EVENT_PULL_REQUEST_TITLE']
pr_author = os.environ['GITHUB_EVENT_PULL_REQUEST_USER_LOGIN']
pr_link = os.environ['GITHUB_EVENT_PULL_REQUEST_HTML_URL']

message = f"New Pull Request:\nTitle: {pr_title}\nAuthor: {pr_author}\nLink: {pr_link}"

payload = {
    'text': message
}
headers = {
    'Content-Type': 'application/json'
}
response = requests.post(webhook_url, json=payload, headers=headers)

if response.status_code == 200:
    print("Notification sent successfully!")
else:
    print("Failed to send notification.")
    print(response.text)
