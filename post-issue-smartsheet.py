import requests
import smartsheet
import logging
import os

SMARTSHEET_ACCESS_TOKEN = os.environ('SMARTSHEET_ACCESS_TOKEN')
JSON_ACCESS = os.environ('JSON_SMARTSHEET_ACCESS_TOKEN')
GITHUB_ACCESS_TOKEN = os.environ('GH_ACCESS_TOKEN')

# Initialize client. Uses the API token in the environment variable 'SMARTSHEET_ACCESS_TOKEN'
smart = smartsheet.Smartsheet()
# Make sure we don't miss any error
smart.errors_as_exceptions(True)

# Log all calls
logging.basicConfig(filename='rwsheet.log', level=logging.INFO)

# GET request to GitHub API
response = requests.get('https://api.github.com/repos/brinkbrink/github-smartsheet-test/issues/5',
                        headers={'Authorization': GITHUB_ACCESS_TOKEN, 
                                 'Content-Type': 'application/vnd.github+json',
                                 'X-GitHub-Api-Version': '2022-11-28'})
issues = response.json()

# for use below--in order to truncate url to use as repo name
repo_url = issues['repository_url']

# POST request to Smartsheet API
smartsheet_response = requests.post(
    'https://api.smartsheet.com/2.0/sheets/2342839996338052/rows',
    headers={'Authorization': JSON_ACCESS, 'Content-Type': 'application/json'},
    json={
        'sheetId': 2342839996338052,
        'accessLevel': 'OWNER',
        'createdBy': {
            'name': 'automation'
        },
        'cells': [
            {
            'columnId': 5558737690382212,
            'displayValue': 'title',
            'value': issues['title']
            },
            {
            'columnId': 3306937876696964,
            'displayValue': 'repo url',
            'value': repo_url[40:]
            },
            {
            'columnId': 7810537504067460,
            'displayValue': 'priority',
            'value': 'priority pull from PBI'
            },
            {
            'columnId': 2181037969854340,
            'displayValue': 'assignee',
            'value': issues['assignee']['login']
            },
            {
            'columnId': 6684637597224836,
            'displayValue': 'index',
            'value': issues['number']
            }
        ]
        })