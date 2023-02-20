from bs4 import BeautifulSoup
import requests

# objeto site recebe o conteúdo da requisição htttp do site
site = requests.get("https://www.climatempo.com.br/").content

soup = BeautifulSoup(site, 'html.parser')

# transforma o html em string o print exibe o html
print(soup.prettify())

# procura primeira etiqueta ( tag )
print(soup.a)

# procurar item no scrapper
print(soup.find('temperatura'))

vento = soup.find("span", class_="-bold -gray-dark-2 -uppercase -font-12 _padding-5")

print(vento.string)
