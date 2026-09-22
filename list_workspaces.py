import os
import requests
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("WEBEX_TOKEN")
headers = {"Authorization": f"Bearer {TOKEN}"}

response = requests.get("https://webexapis.com/v1/workspaces", headers=headers)
workspaces = response.json()["items"]

for ws in workspaces:
    print(f"{ws['displayName']} — capacity: {ws.get('capacity', 'n/a')}")