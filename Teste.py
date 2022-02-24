import pandas as pd

dados = pd.read_csv('dados/aluguel.csv', sep=';')
#print(dados)

#json = open('dados/aluguel.json')
df_json = pd.read_json('dados/aluguel.json')
#print(df_json)

df_txt = pd.read_table('dados/aluguel.txt')
#print(df_txt)

df_xlsx = pd.read_excel('dados/aluguel.xlsx')
#print(df_xlsx)

df_html = pd.read_html('dados/dados_html_1.html')
print(df_html[0])