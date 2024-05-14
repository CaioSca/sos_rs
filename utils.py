from clients import connect_spreadsheet_api, connect_to_drive_api


def get_worksheet_object(spreadsheet_id: str, worksheet_index: int):
    client = connect_spreadsheet_api()

    spreadsheet = client.open_by_key(spreadsheet_id)
    worksheet = spreadsheet.get_worksheet(worksheet_index)

    return worksheet


def upload_file_to_drive(file_path: str, drive_folder_id: str):
    drive = connect_to_drive_api()

    file = drive.CreateFile({'title': file_path.split('/')[-1], 'parents': [{'id': drive_folder_id}]})
    file.SetContentFile(file_path)
    file.Upload()

    print(f"File {file_path} uploaded to Google Drive with ID: {file['id']}")
