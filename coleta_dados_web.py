import requests
from bs4 import BeautifulSoup

url= 'https://wiki-python-org.translate.goog/moin/FrontPage?_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=pt&_x_tr_pto=tc'
requisicao= requests.get(url)
extracao= BeautifulSoup(requisicao.text, features= 'html.parser')

#Exibir o testo
#print(extracao.text.strip())

# for linha_texto in extracao.find_all('h2'):
#     titulo = linha_texto.text.strip()
#     print('titulo: ', titulo)

# Contar títulos  e parágrafos
# contar_titulos = 0
# contar_paragrafos = 0
#
# for linha_texto in extracao.find_all('h2','p'):
#     if linha_texto.name == 'h2':
#         contar_titulos += 1
#     else:
#         contar_paragrafos += 1
#
# print("Total de títulos: ", contar_titulos)
# print("Total de parágrafos: ", contar_paragrafos)

#Exibir somente o texto das tags h2 e p
# for linha_texto in extracao.find_all('h2','p'):
#     if linha_texto.name == 'h2':
#         titulo= linha_texto.text.stip()
#         print('Título: \n', titulo)
#     else:
#         paragrafo = linha_texto.text.stip()
#         print('Parágrafo: \n', paragrafo)

#Exibir tags aninhadas
for titulo in extracao.find_all('h2'):
        print('\n Título: ', titulo.text.strip())
        for link in titulo.find_next_siblings('p'):
            for a in link.find_all('a', href=True):
                print('Texto Link: ', a.text.strip(), ' | URL:', a["href"])
