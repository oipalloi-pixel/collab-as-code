import os
import requests
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("WEBEX_TOKEN")
headers = {"Authorization": f"Bearer {TOKEN}"}

response = requests.get("https://webexapis.com/v1/people/me", headers=headers)
data = response.json()

print(f"Name: {data['displayName']}")
print(f"Email: {data['emails'][0]}")