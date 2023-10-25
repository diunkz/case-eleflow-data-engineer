import pandas as pd
import os

# Diretório onde estão os arquivos CSV
diretorio = './data_engineer_test/AIR_CIA/'

# Defina os nomes das colunas no DataFrame total, se necessário
nomes_colunas = ['razao_social', 'icao_iata', 'cnpj', 'atividades_aereas',
                 'endereco_sede', 'telefone', 'email', 'decisao_operacional', 
                 'data_decisao_operacional', 'validade_operacional']

# Inicialize um DataFrame vazio para armazenar os dados
df_total = pd.DataFrame()

# Liste todos os arquivos CSV na pasta
for filename in os.listdir(diretorio):
    if filename.endswith(".csv"):
        # Crie o caminho completo para o arquivo
        arquivo = os.path.join(diretorio, filename)
        
        # Leia o arquivo CSV e adicione os dados ao DataFrame total
        df = pd.read_csv(arquivo, sep=';')
        df_total = pd.concat([df_total, df], ignore_index=True)


df_total.columns = nomes_colunas

df_total[['icao', 'iata']] = df_total['icao_iata'].str.split(n=1, expand=True)

posicao_icao_iata = nomes_colunas.index('icao_iata')
nomes_colunas.pop(posicao_icao_iata)
nomes_colunas.insert(posicao_icao_iata, 'icao')
nomes_colunas.insert(posicao_icao_iata + 1, 'iata')

df_total = df_total[nomes_colunas]
df_total = df_total.where(pd.notna(df_total), None)
print(df_total.columns)

print(df_total)


# eliminar duplicatas
# df_total = df_total.drop_duplicates()

linhas_duplicadas = df_total[df_total.duplicated()]
# Exiba o DataFrame total
print(df_total)
print(linhas_duplicadas)