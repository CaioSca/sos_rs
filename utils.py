from clients import connect_google_api

def get_worksheet_object(spreadsheet_id: str, worksheet_index: int):
    client = connect_google_api()

    spreadsheet = client.open_by_key(spreadsheet_id)
    worksheet = spreadsheet.get_worksheet(worksheet_index)

    return worksheet