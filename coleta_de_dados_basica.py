from io import StringIO
import requests
from bs4 import BeautifulSoup
import pandas

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Languege": "en-US,en;q=0.9"
}
print("Request")
#response = requests.get('https://finance.yahoo.com/quote/%5EBVSP/history', headers=headers)
response = requests.get('https://webscraper.io/test-sites/tables/tables-semantically-correct', headers=headers)
print(response.text[:600])


print("BeautifulSoup")
soup = BeautifulSoup(response.text, features='html.parser')
print(soup.prettify()[:1000])

print("Pandas: ")
url_dados = pandas.read_html(response.text)
print(url_dados[0].head(10))

