from google.oauth2.service_account import Credentials
import gspread

class Gsheet:
    def __init__(self, creds_path, sheet_name):
        self.creds_path = creds_path
        self.sheet_name = sheet_name
        self.client = None
        self.authenticate()

    def authenticate(self):
        scopes = [
            'https://www.googleapis.com/auth/spreadsheets',
            'https://www.googleapis.com/auth/drive'
        ]
        creds = Credentials.from_service_account_file(self.creds_path, scopes=scopes)
        self.client = gspread.authorize(creds)


    def write_data(self, data):
        keys = ['id', 'publishedAt', 'salary', 'title', 'jobUrl', 'companyName', 'companyUrl', 'location', 'postedTime', 'applicationsCount', 'description', 'contractType', 'experienceLevel', 'workType', 'sector', 'companyId', 'posterProfileUrl', 'posterFullName']
        data_lists = [[entry[key] for key in keys] for entry in data]
        sheet = self.client.open(self.sheet_name).sheet1
        sheet.append_rows(data, value_input_option='USER_ENTERED')