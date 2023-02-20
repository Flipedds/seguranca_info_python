import socket

conexao = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Cliente: Socket Criado com Sucesso !!!!")

host = 'localhost'
port = 5433

mensagem = 'Olá servidor, Tudo bem?'

try:
    print("Cliente: " + mensagem)
    # Empacotar mensagem e enviar como udp para o servidor
    conexao.sendto(mensagem.encode(), (host, 5432))

    dados, servidor = conexao.recvfrom(4096)
    dados = dados.decode()
    print("Mensagem enviada: " + dados)
finally:
    print('Cliente: Fechando a Conexão')
    conexao.close()
