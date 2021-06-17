import requests
from dnac_config import process_args
from authenticate import get_token
from dnac_config import process_args
import json
import sys


def get_issues(dnac):
   url = f"https://{dnac}/dna/intent/api/v1/issues"
   
   apList =[]
   headers = {
       "Content-Type": "application/json",
       "Accept": "application/json",
       "X-auth-Token": token,
   }
   response =  requests.get(url, headers=headers, verify=False).json()

   return(response)

def print_issues(issue_data):
   json_formatted = json.dumps(issue_data, indent=2)
   print(json_formatted)

if __name__ == "__main__":
   #process DNAC arguments
   dnac_parameters = process_args(sys.argv)
   #authenticate and get token
   token = get_token(dnac_parameters)
   #Get Events of Interest
   issue_data = get_issues(dnac_parameters['host'])
   print_issues(issue_data)

