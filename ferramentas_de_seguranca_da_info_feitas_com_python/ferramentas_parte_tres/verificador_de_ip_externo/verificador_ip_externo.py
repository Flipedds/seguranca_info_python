import re
import json
from urllib.request import urlopen

url = 'https://ipinfo.io/json'

resposta = urlopen(url)

# tras os dados relacionados ao seu ip externo em fomato de dicionário
dados = json.load(resposta)

ip = dados['ip']
cidade = dados['city']
regiao = dados['region']
pais = dados['country']
provedor = dados['org']
zona = dados['timezone']

print(f" Ip:{ip}\n Cidade: {cidade}\n Região: {regiao}\n País:{pais}\n Provedor: {provedor}")

