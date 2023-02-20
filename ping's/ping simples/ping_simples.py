import os

"""
Verificar resposta de um ip ou host
Realiza um ping
"""
ip_ou_host = input("digite o ip ou host a ser verificado: ")

# Necessita de privilégios de administrador para executar esse comando
# Se não funcionar procurar em path e adicionar C:\Windows\System32 nas variaveis de ambiente
os.system(f'ping -n 6 {ip_ou_host}')

