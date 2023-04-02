import random

alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
configuracao = list()
for char in alfabeto:
    configuracao.append(char.lower())

random.shuffle(configuracao)

def pos_alfabeto(val):
    return ord(val) - ord('a')

def encriptar(val):
    callback = ''
    for char in val:
        if not char == ' ':
            callback += str(configuracao[pos_alfabeto(char)])
        else:
            callback += ' '
    print(callback)

valor = str(input("Digite o texto a ser encriptado: "))
encriptar(valor.lower())
print(configuracao)
