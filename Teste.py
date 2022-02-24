import pandas as pd

dados = pd.read_csv('dados/aluguel.csv', sep=';')

json = open('dados/aluguel.json')
print(json.read())