import itertools

string = input('String a ser permutada: ')

# permuta os caracteres e forma uma palavra com a quantidade de caracteres escolhido
resultados = itertools.permutations(string, len(string))

# para cada resultado em resultados mostre a junção do resultado
for resultado in resultados:
    print(''.join(resultado))
