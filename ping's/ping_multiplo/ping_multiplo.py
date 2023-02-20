import os
import time
# Abre o arquivo hosts.txt
with open('hosts.txt') as file:
    dump = file.read()
    dump = dump.splitlines()
    for ip in dump:
        print('-' * 60)
        print('Verificando o ip:', ip)
        print('-'*60)
        # Necessita de privilégios de administrador para executar esse comando
        # Se não funcionar procurar em path e adicionar C:\Windows\System32 nas variaveis de ambiente
        os.system('ping -n 2 ' + ip)
        time.sleep(5)
