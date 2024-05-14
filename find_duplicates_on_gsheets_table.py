import os
import pandas as pd
import re
import unicodedata

from datetime import datetime
from models import FormularioNovosAbrigos, PlanilhaCentral, SOSMinutoAMinuto
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics.pairwise import cosine_similarity
from utils import upload_file_to_drive


def normalize_strings(string: str):
    string = unicodedata.normalize('NFKD', string).encode('ascii', 'ignore').decode('utf-8')
    string = string.lower().strip()
    string = re.sub(r'\s+', ' ', string)
    
    return string


def cluster_labels(df_cadastro_abrigos_preenchidos: pd.DataFrame, column_label: str):
    vectorizer = TfidfVectorizer(min_df=1, analyzer='char_wb', ngram_range=(2, 5))
    tf_idf_matrix = vectorizer.fit_transform(df_cadastro_abrigos_preenchidos[column_label])

    cosine_sim = cosine_similarity(tf_idf_matrix)
    cosine_dist = 1 - cosine_sim  

    clustering = AgglomerativeClustering(n_clusters=None, distance_threshold=0.7, linkage='average')
    labels = clustering.fit_predict(cosine_dist)

    return labels


def main(modelos, colunas_labels_analisar, colunas_limpar_nulos, nomes_arquivos):
    df = modelos.get_spreadsheet_table()
    
    df_preenchidos = df[df[colunas_limpar_nulos] != '']

    df_preenchidos['nome_normalizado'] = df_preenchidos[colunas_labels_analisar].apply(normalize_strings)

    labels = cluster_labels(df_preenchidos, 'nome_normalizado')

    df_preenchidos['agrupamentos'] = labels
    df_preenchidos.sort_values(by='agrupamentos', inplace=True)
    
    date_now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    file_name = f'{nomes_arquivos}_{date_now}.xlsx'
    df_preenchidos.to_excel(file_name, index=False)

    upload_file_to_drive(file_name, '1wCQQtuS0M-Qbq2cwHJXE9ncfhzFvDYAT')
    os.remove(file_name)


modelos = [FormularioNovosAbrigos, PlanilhaCentral, SOSMinutoAMinuto]
colunas_limpar_nulos = ['Carimbo de data/hora', 'NOME DA INSTITUIÇÃO', 'Nome do Abrigo']
colunas_labels_analisar = ['NOME', 'NOME DA INSTITUIÇÃO', 'Nome do Abrigo']
nomes_arquivos = ['sos_rs_forms_cadastro_novos_abrigos', 'sos_rs_forms_planilha_central', 'sos_rs_minuto_a_minuto']

for modelo, coluna_limpar_nulo, coluna_label, nome_arquivo in zip(
    modelos, 
    colunas_limpar_nulos, 
    colunas_labels_analisar, 
    nomes_arquivos
    ):
    main(modelo, coluna_label, coluna_limpar_nulo, nome_arquivo)

