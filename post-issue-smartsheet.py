import requests
import smartsheet
import logging
#import os


# Initialize client. Uses the API token in the environment variable "SMARTSHEET_ACCESS_TOKEN"
smart = smartsheet.Smartsheet()
# Make sure we don't miss any error
smart.errors_as_exceptions(True)

# Log all calls
logging.basicConfig(filename='rwsheet.log', level=logging.INFO)

# GET request to GitHub API
response = requests.get('https://api.github.com/repos/brinkbrink/github-smartsheet-test/issues',
                        headers={'Authorization': 'Bearer YOUR_ACCESS_TOKEN', 
                                 'Content-Type': 'application/vnd.github+json',
                                 'X-GitHub-Api-Version': '2022-11-28'})
issues = response.json()

# POST request to Smartsheet API
smartsheet_response = requests.post(
    'https://api.smartsheet.com/2.0/sheets/2342839996338052/rows',
    headers={'Authorization': 'Bearer YOUR_ACCESS_TOKEN', 'Content-Type': 'application/json'},
    json={'rows': [{'cells': [{'columnId': 5558737690382212, 'value': requests.title}]}]}
)
