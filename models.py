import pandas as pd
from utils import get_worksheet_object


class FormularioNovosAbrigos:
    def get_spreadsheet_table():
        ws_object = get_worksheet_object(spreadsheet_id='15uj1HsbQKNT5PvFGFPkmTpFFpvg67W41NqZy5g8K-ss', worksheet_index=0)
        
        df = pd.DataFrame(ws_object.get_all_values())
        df.columns = df.iloc[1]
        df = df[2:]
        
        return df


class PlanilhaCentral:
    def get_spreadsheet_table():
        ws_object = get_worksheet_object(spreadsheet_id='1lTY_EHKyw8uDs31yY0mogmaNrdNM_uitnsslWx1gXUw', worksheet_index=0)
        
        df = pd.DataFrame(ws_object.get_all_values())
        df.columns = df.iloc[1]
        df = df[8:]
            
        return df


class SOSMinutoAMinuto:
    def get_spreadsheet_table():
        ws_object = get_worksheet_object(spreadsheet_id='1in0aRAkfTSfZLLCdLh_UDEb0RjunEuKsMz-9cUT7joU', worksheet_index=0)
        
        df = pd.DataFrame(ws_object.get_all_values())
        df.columns = df.iloc[0]
        df = df[1:]
            
        return df
