import requests

# GET request to GitHub API
response = requests.get('https://api.github.com/repos/{owner}/{repo}/issues')
issues = response.json()

# POST request to Smartsheet API
smartsheet_response = requests.post(
    'https://api.smartsheet.com/2.0/sheets/{sheet_id}/rows',
    headers={'Authorization': 'Bearer YOUR_ACCESS_TOKEN', 'Content-Type': 'application/json'},
    json={'rows': [{'cells': [{'columnId': your_column_id, 'value': issue['title']}]}]}
)
