import socket
import sys


def main():
    try:
        """ Tenta conectar a porta de um host ou ip """
        conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

    except socket.error as e:

        print("A conexão falhou")
        print("Erro: {}".format(e))
        # finaliza
        sys.exit()
    print("Socket criado com sucesso")

    host_alvo = input("Digite o Host ou ip a ser conectado: ")
    porta_alvo = input('Digite a porta a ser conectada: ')

    try:
        conexao.connect((host_alvo, int(porta_alvo)))
        print("Cliente TCP conectado com Sucesso no host: " + host_alvo + " e na porta: " + porta_alvo)
        conexao.shutdown(2)
    except socket.error as e:
        print("Não foi possível conectar no host: " + host_alvo + " e na porta: " + porta_alvo)
        print("Erro: {}".format(e))
        # finaliza
        sys.exit()


if __name__ == "__main__":
    main()
