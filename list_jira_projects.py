import requests
from requests.auth import HTTPBasicAuth
import json, os
from dotenv import load_dotenv

load_dotenv()

url = "https://navjyotsinghpulaha.atlassian.net/rest/api/3/poject"

auth = HTTPBasicAuth(os.getenv("EMAIL_ID"), os.getenv("JIRA_API_TOKEN"))

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output = json.loads(response.text)
print(f'Below are the project names that you have in {os.getenv("EMAIL_ID")} account in JIRA')
i = 1
for project_name in output:
    print(f"{i}. {project_name['name']}")
    i+=1
