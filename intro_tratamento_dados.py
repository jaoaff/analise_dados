import pandas as pd

df = pd.read_csv('clientes.csv')

#verifica os primeiros registros
print(df.head().to_string())

#verifica quantidade de linha e colunas
print('Qtd: ', df.shape)

#verifica tipos de dados
print('Tipagens:\n', df.dtypes)

#checar valores nulos
print('Valores nulos:\n', df.isnull().sum())
