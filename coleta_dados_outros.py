import pymysql as my
import pandas as pd
from sqlalchemy import create_engine

def conexao_sql(host, user, password, db, table):
    #criar conexão
    conn = my.connect(host=host, user=user, password=password, db=db)

    cursor = conn.cursor()

    #Executar consulta
    query = 'SELECT * FROM ' + table + ' limit 10'
    cursor.execute(query)

    #Buscar resultado
    resultados = cursor.fetchall()

    #Exibir os resultados
    print('Tbela MySQL: ')
    for linha in resultados:
        print(linha)

    #Fechar conexão
    cursor.close()
    conn.close()

def df_conexao_mysql(host, user, password, db, table):
    #Criar conexão
    conn = create_engine('mysql+pymysql://' + user + ':' + password + '@' + host + '/' + db)


    #Execuratar consulta e armazenar em um dataframe
    query = 'SELECT * FROM ' + table
    df = pd.read_sql(query, conn)

    #Exibir os resultados
    print('Tabela MySQL com dataframe: \n', df.head())

    #Fechar conexão
    conn.dispose()
    return df

def conexao_excel(path):
    # Ler arquivo Excel
    df = pd.read_excel(path)
    print('Dados Excel: \n', df.head())

    # Escrever arquivo csv
    df.to_csv('dados.csv', index=False)


def conexao_csv(path):
    # Ler arquivo csv
    df = pd.read_csv(path)
    print('Dados csv: \n', df.head())

    # Escrever aquivo json
    df.to_json('dados.json', orient='records', index=False)


#conexao_sql('localhost', 'root','1234', 'loja_informatica', 'cliente')
df_cliente = df_conexao_mysql('localhost', 'root','1234', 'loja_informatica', 'cliente')
df_cliente.to_excel('dados.xlsx', index=False)

conexao_excel('dados.xlsx')

conexao_csv('dados.csv')