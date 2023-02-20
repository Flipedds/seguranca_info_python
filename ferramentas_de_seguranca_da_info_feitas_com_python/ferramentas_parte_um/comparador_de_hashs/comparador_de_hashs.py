import hashlib

arquivo_um = 'arquivo_um.txt'
arquivo_dois = 'arquivo_dois.txt'

hash_um = hashlib.new('ripemd160')

hash_um.update(open(arquivo_um, 'rb').read())

hash_dois = hashlib.new('ripemd160')

hash_dois.update(open(arquivo_dois, 'rb').read())

if hash_um.digest() != hash_dois.digest():
    print(f'O Arquivo: {arquivo_um} é diferente do arquivo: {arquivo_dois}')
    print(f'O hash do arquivo {arquivo_um} é: ', hash_um.hexdigest())
    print(f'O hash do arquivo {arquivo_dois} é: ', hash_dois.hexdigest())
else:
    print(f'O Arquivo: {arquivo_um} é igual ao arquivo: {arquivo_dois}')
    print(f'O hash do arquivo {arquivo_um} é: ', hash_um.hexdigest())
    print(f'O hash do arquivo {arquivo_dois} é: ', hash_dois.hexdigest())