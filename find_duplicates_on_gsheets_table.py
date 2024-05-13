import re
import unicodedata

from models import FormularioNovosAbrigos
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics.pairwise import cosine_similarity


def normalize_string(string: str):
    string = unicodedata.normalize('NFKD', string).encode('ascii', 'ignore').decode('utf-8')
    string = string.lower().strip()
    string = re.sub(r'\s+', ' ', string)
    return string


df_cadastro_abrigos = FormularioNovosAbrigos.get_spreadsheet_table()
df_cadastro_abrigos = df_cadastro_abrigos[df_cadastro_abrigos['Email:'] != '']

df_cadastro_abrigos['NOME'] = df_cadastro_abrigos['NOME'].apply(normalize_string)

vectorizer = TfidfVectorizer(min_df=1, analyzer='char_wb', ngram_range=(2, 5))
tf_idf_matrix = vectorizer.fit_transform(df_cadastro_abrigos['NOME'])

cosine_sim = cosine_similarity(tf_idf_matrix)
cosine_dist = 1 - cosine_sim  

clustering = AgglomerativeClustering(n_clusters=None, distance_threshold=0.7, linkage='average')
labels = clustering.fit_predict(cosine_dist)

df_cadastro_abrigos['agrupamentos'] = labels

df_cadastro_abrigos.sort_values(by='agrupamentos', inplace=True)

df_cadastro_abrigos.to_excel('agrupamentos_abrigos.xlsx', index=False)


