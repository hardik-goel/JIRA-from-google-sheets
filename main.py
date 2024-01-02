from cryptography.fernet import Fernet
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from jira import JIRA

def load_key():
    return open("key.key", "rb").read()

def decrypt_password(encrypted_password, key):
    f = Fernet(key)
    decrypted_password = f.decrypt(encrypted_password)
    return decrypted_password.decode()

key = load_key()

encrypted_password = b''  # replace with your encrypted password
decrypted_password = decrypt_password(encrypted_password, key)


#
# Use the JSON key file you downloaded when you created your Google Sheets API service account
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
# json file path
creds = ServiceAccountCredentials.from_json_keyfile_name('', scope)
client = gspread.authorize(creds)

spreadsheet = client.open('<SHEETNAME>')

# Get the specific sheet
sheet = spreadsheet.worksheet('sheet')

# Get all records of the data
data = sheet.get_all_records()

options = {
    'server': '<JIRASERVERNAME>',
    'verify': False
}
jira = JIRA(basic_auth=('<USERNAME>', decrypted_password), options=options)

# Iterate over the data and create JIRA issues
for index, row in enumerate(data, start=2):  # start=2 because Google Sheets rows are 1-indexed and we skip the header row
    # Check if the 'JIRA ID' column is empty
    if not row['JIRA']:
        summary = row['Summary'].replace('\n', ' ')
        issue_dict = {
            'project': {'key': 'PROJECTNAME'},
            'summary': summary,
            'description': row['Description'],
            'issuetype': {'name': 'Task'},
            'customfield_19804': {'value': '<VALUE>'},
            'customfield_19805': [{'value': '<VALUE2>'}],
            'assignee': {'name': row['Assignee']},
        }
        issue = jira.create_issue(issue_dict)
        # Get the issue key
        issue_key = issue.key

        # Add the issue key to the corresponding row in the Google Sheet
        sheet.update_cell(index, len(row), issue_key)

print ("JIRA successfully created and JIRA number captured in google sheet")
