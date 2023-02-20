from threading import Thread
import time


def carro(velocidade, piloto):
    """

    :param velocidade: velocidade do carro
    :param piloto: nome do piloto
    :return: None
    """
    trajeto = 0
    while trajeto <= 99:
        trajeto += velocidade
        time.sleep(0.5)
        print('Piloto: {} km: {} \n'.format(piloto, trajeto))


# Define a thread
t_carro_um = Thread(target=carro, args=[10, 'python'])
t_carro_dois = Thread(target=carro, args=[20, 'filipe'])

# Inicia a thread
t_carro_um.start()
t_carro_dois.start()
