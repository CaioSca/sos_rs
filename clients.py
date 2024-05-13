import gspread
from oauth2client.service_account import ServiceAccountCredentials


def connect_google_api():
    """Cria a variável Client, utilizada nas requisições à API Google."""
    scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]

    credentials = ServiceAccountCredentials.from_json_keyfile_name("service_account.json", scope)
    client = gspread.authorize(credentials)

    return client
