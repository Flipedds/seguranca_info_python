import random
import string

tamanho = int(input('digite o tamanho de senha que você deseja: '))

chars = string.ascii_letters + string.digits + 'ç!@#$%?'

random = random.SystemRandom()

print(''.join(random.choice(chars) for i in range(tamanho)))

