import pandas as pd
from utils import get_worksheet_object


class FormularioNovosAbrigos:
    def get_spreadsheet_table():
        ws_object = get_worksheet_object(spreadsheet_id='15uj1HsbQKNT5PvFGFPkmTpFFpvg67W41NqZy5g8K-ss', worksheet_index=0)
        
        df = pd.DataFrame(ws_object.get_all_values())
        df.columns = df.iloc[1]
        df = df[2:]
        
        return df
