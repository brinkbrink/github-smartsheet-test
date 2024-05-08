import requests
import smartsheet
import logging
import os
from dotenv import load_dotenv

load_dotenv()

SMARTSHEET_ACCESS_TOKEN = os.getenv('SMARTSHEET_ACCESS_TOKEN')
os.environ['SMARTSHEET_ACCESS_TOKEN'] = SMARTSHEET_ACCESS_TOKEN
JSON_ACCESS = os.getenv('JSON_SMARTSHEET_ACCESS_TOKEN')
GITHUB_ACCESS_TOKEN = os.getenv('GITHUB_ACCESS_TOKEN')

# Initialize client. Uses the API token in the environment variable 'SMARTSHEET_ACCESS_TOKEN'
smart = smartsheet.Smartsheet()
# Make sure we don't miss any error
smart.errors_as_exceptions(True)

# Log all calls
logging.basicConfig(filename='rwsheet.log', level=logging.INFO)

# GET request to GitHub API
response = requests.get('https://api.github.com/repos/brinkbrink/github-smartsheet-test/issues/1',
                        headers={'Authorization': GITHUB_ACCESS_TOKEN, 
                                 'Content-Type': 'application/vnd.github+json',
                                 'X-GitHub-Api-Version': '2022-11-28'})
issues = response.json()


# POST request to Smartsheet API
smartsheet_response = requests.post(
    'https://api.smartsheet.com/2.0/sheets/2342839996338052/rows',
    headers={'Authorization': JSON_ACCESS, 'Content-Type': 'application/json'},
    json={
        'sheetId': 2342839996338052,
        'accessLevel': 'OWNER',
        'createdAt': '2019-08-24T14:15:22Z',
        'createdBy': {
            'email': 'jane.doe@smartsheet.com',
            'name': 'Jane Doe'
        },
        'cells': [
            {
            'columnId': 5558737690382212,
            'displayValue': 'test1',
            'value': issues['title']
            },
            {
            'columnId': 3306937876696964,
            'displayValue': 'test1',
            'value': 'IS THIS'
            },
            {
            'columnId': 7810537504067460,
            'displayValue': 'test1',
            'value': 'working for'
            },
            {
            'columnId': 2181037969854340,
            'displayValue': 'test1',
            'value': '??'
            }
        ],
        'modifiedAt': '2019-08-24T14:15:22Z',
        'modifiedBy': {
            'email': 'jane.doe@smartsheet.com',
            'name': 'Jane Doe'
        }
        })