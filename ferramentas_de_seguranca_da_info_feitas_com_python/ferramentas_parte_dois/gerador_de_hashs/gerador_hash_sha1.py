import hashlib

string = input("digite o texto para gerar um hash: ")
resultado = hashlib.sha1(string.encode('utf8'))

print('O hash da string é: {}'.format(resultado.hexdigest()))