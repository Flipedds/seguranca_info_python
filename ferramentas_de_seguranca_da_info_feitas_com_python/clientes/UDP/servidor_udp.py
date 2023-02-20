import socket

conexao = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Socket Criado com Sucesso !!!")

host = 'localhost'
port = 5432

conexao.bind((host, port))
mensagem = '\nServidor: Olá Cliente e aí, beleza??'

while 1:
    dados, endereco = conexao.recvfrom(4096)

    if dados:
        print('Servidor enviando mensagem......')
        conexao.sendto(dados + (mensagem.encode()), endereco)
