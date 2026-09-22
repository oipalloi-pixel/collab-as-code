import os
import csv
import requests
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("WEBEX_TOKEN")
headers = {"Authorization": f"Bearer {TOKEN}"}

response = requests.get("https://webexapis.com/v1/workspaces", headers=headers)
workspaces = response.json()["items"]

with open("workspace_report.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Capacity", "Type"])
    for ws in workspaces:
        writer.writerow([ws["displayName"], ws.get("capacity", "n/a"), ws.get("type", "n/a")])

print(f"Report written for {len(workspaces)} workspaces.")