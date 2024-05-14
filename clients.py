import gspread
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from oauth2client.service_account import ServiceAccountCredentials


def connect_spreadsheet_api():
    """Cria a variável Client, utilizada nas requisições à API do Sheets."""
    scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]

    credentials = ServiceAccountCredentials.from_json_keyfile_name("service_account.json", scope)
    client = gspread.authorize(credentials)

    return client


def connect_to_drive_api():
    """Cria a variável Client, utilizada nas requisições à API do Drive."""
    scope = ['https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('service_account.json', scope)

    gauth = GoogleAuth()
    gauth.credentials = credentials

    drive = GoogleDrive(gauth)
    
    return drive
