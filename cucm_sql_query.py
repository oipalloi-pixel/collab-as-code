import os
from dotenv import load_dotenv
from cisco.collab.ucm.sdk import PATHS
from cisco.collab.ucm.sdk.template import AxlTemplate
import urllib3

# Suppress insecure request warnings for self-signed certificates
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

load_dotenv()

# Initialize the SDK
axl = AxlTemplate(
    host=os.getenv("CUCM_HOST"),
    username=os.getenv("CUCM_USER"),
    password=os.getenv("CUCM_PASS"),
    wsdl_path=PATHS.WSDL.AXL.V12_5,
    verify=False,
)

# Querying locations using SQL
sql_result = axl.sql("select id, name from location")

print("--- Defined Locations ---")
for location in sql_result:
    print(f"ID: {location['id']}, Name: {location['name']}")