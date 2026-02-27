import pandas as pd
import numpy as np
from scipy import stats

pd.set_option('display.max_columns', None)

df= pd.read_csv('clientes-v2.csv')

print(df.head())

# Transformação Logaritmica
df['salario_log'] = np.log1p(df['salario']) # log1p é usado para evitar problemas com valores zero

print("\nDataFrame após transformação no 'salario':\n", df.head())

# Trasformação Box-Cox
df['salario_boxcox'] = stats.boxcox(df['salario'] + 1)

print("\nDataFrame após transformação Box-Cox no 'salario':\n", df.head())

# Codificação de Frequencia para 'estado'
estado_freq = df['estado'].value_counts() / len(df)
df['estado_freq'] = df['estado'].map(estado_freq)

print("\nDataFrame após condificação de frequencia para 'estado':\n", df.head())

# Interações
df['interacao_idade_filhos'] = df['idade'] * df['numero_filhos']

print("\nDataFrame após criação de  interações entre 'idae' e 'numero_filhos':\n", df.head())


