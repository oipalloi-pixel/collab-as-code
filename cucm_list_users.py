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

# List users
response = axl.listUser(
    searchCriteria={"userid": "%"},
    returnedTags={"userid": "", "firstName": "", "lastName": ""}
)

users = response["user"] if isinstance(response, dict) else response.user

for user in users:
    print(f"User ID: {user['userid']}, Name: {user.get('lastName', '')}, {user.get('firstName', '')}")