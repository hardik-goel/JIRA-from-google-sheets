The utility aims to create an automatic JIRA from google sheets.
This becomes very handy as creating a JIRA becomes an additional overhead when you 
are anyway maintaining the status over google sheet.
If a JIRA is created then no duplicate JIRAs would be created.

Attached is the snippet (can be found in resources directory) of a sample set of columns to be provided corresponding to which a 
JIRA would be created and catured in the sheet itself.

Use the password_encryption file to encrypt your password which 
could be plugged iun the main file.

Pre-requisites:
Enable the API. 
Create service account and download the key JSON file.
Should have JIRA server name details handy
Provide access to the email in service account

TODO:
Parameterisation creating config files to avoid hardcoding. 
Honestly, didn't want to invest much into this simple utility :P



