import os
import json
import pandas as pd

#funções auxiliares
def ler_jsons(diretorio):
    arquivos_json = [arquivo for arquivo in os.listdir(diretorio) if arquivo.endswith('.json')]

    for nome_arquivo in arquivos_json:
        caminho_arquivo = os.path.join(diretorio, nome_arquivo)
        with open(caminho_arquivo, 'r', encoding='utf-8-sig') as arquivo:
            yield json.load(arquivo)

# nome das colunas em snake_case
nomes_colunas = ['icao_empresa_aerea', 'numero_voo', 'codigo_autorizacao', 'codigo_tipo_linha',
                  'icao_aerodromo_origem', 'icao_aerodromo_destino', 'partida_prevista',
                  'partida_real', 'chegada_prevista', 'chegada_real', 'situacao_voo', 'codigo_justificativa']

# Diretório onde estão os arquivos JSON
diretorio_vra = './data_engineer_test/VRA'

# Criar um gerador
vra_generator = ler_jsons(diretorio_vra)

#criação do dataframe com os dados de vra
vra_df = pd.DataFrame()

# adicionando informações de cada arquivo JSON no dataframe
for lista_de_dicts in vra_generator:
    vra_df = vra_df._append(lista_de_dicts, ignore_index=True)

# modificando nome das colunas do dataframe VRA
vra_df.columns = nomes_colunas
# vra_df = vra_df.drop_duplicates()

vra_df = vra_df.where(pd.notna(vra_df), None)
print(vra_df.head(5))
# print(vra_df.columns)
# print(vra_df.shape)
# icao_unicos = pd.concat([vra_df['icao_aerodromo_origem'], vra_df['icao_aerodromo_destino']]).unique()

# print(icao_unicos)