import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)

gc = gspread.authorize(creds)
ws = gc.open_by_key('11JkQmkecYDaXyBcE4pT7TzPVotw5ARFnDD6Z_e0KuwI').sheet1

values = ws.get_all_records()
print(values)