import requests
import smartsheet
import logging
import os

SMART_ACCESS_TOKEN = os.environ['SMART_ACCESS_TOKEN']
GITHUB_ACCESS_TOKEN = os.environ['GH_ACCESS_TOKEN']
ISSUE_NUM = os.environ.get('ISSUE_NUM')

if not ISSUE_NUM:
    raise ValueError("ISSUE_NUM environment variable is not set or is empty.")

# Initialize client. Uses the API token in the environment variable 'SMARTSHEET_ACCESS_TOKEN'
smart = smartsheet.Smartsheet(SMART_ACCESS_TOKEN)
# Make sure we don't miss any error
smart.errors_as_exceptions(True)

# Log all calls
logging.basicConfig(filename='rwsheet.log', level=logging.INFO)

# GET request to GitHub API
response = requests.get(
    f'https://api.github.com/repos/brinkbrink/github-smartsheet-test/issues/{ISSUE_NUM}',
    headers={
        'Authorization': f'token {GITHUB_ACCESS_TOKEN}', 
        'Content-Type': 'application/vnd.github+json',
        'X-GitHub-Api-Version': '2022-11-28'
    }
)

if response.status_code != 200:
    raise Exception(f"GitHub API request failed with status code {response.status_code}")

issues = response.json()

# Check if 'repository_url' is in the response
repo_url = issues.get('repository_url', 'N/A')

# POST request to Smartsheet API
smartsheet_response = requests.post(
    'https://api.smartsheet.com/2.0/sheets/2342839996338052/rows',
    headers={
        'Authorization': f'Bearer {SMART_ACCESS_TOKEN}', 
        'Content-Type': 'application/json'
    },
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
                'value': issues.get('title', 'No Title')
            },
            {
                'columnId': 3306937876696964,
                'displayValue': 'repo url',
                'value': repo_url[40:] if repo_url != 'N/A' else 'No Repo URL'
            },
            {
                'columnId': 7810537504067460,
                'displayValue': 'priority',
                'value': 'priority pull from PBI'
            },
            {
                'columnId': 2181037969854340,
                'displayValue': 'assignee',
                'value': issues.get('assignee', {}).get('login', 'No Assignee')
            },
            {
                'columnId': 6684637597224836,
                'displayValue': 'index',
                'value': issues.get('number', 'No Number')
            }
        ]
    }
)