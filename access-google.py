import google.auth
from google.oauth2 import service_account
import google.auth.transport.requests
import googleapiclient.discovery
import json

# Set the service account credentials
credentials = service_account.Credentials.from_service_account_file('credentials.json')

# Set the Google Sheets API client
sheets_service = googleapiclient.discovery.build('sheets', 'v4', credentials=credentials)

# Set the ID of the spreadsheet
spreadsheet_id = 'spreadsheet_id'

# Set the range of cells to get
range_ = 'Sheet1!A1:Z'

# Get the values from the specified range
result = sheets_service.spreadsheets().values().get(
  spreadsheetId=spreadsheet_id, range=range_).execute()
values = result.get('values', [])

# Convert the values to JSON
json_data = json.dumps(values)

# Print the JSON data
print(json_data)
