import nltk, random, time
nltk.download('words')
from nltk.corpus import words
palavras = words.words('en')

alfabeto = "abcdefghijklmnopqrstuvwxyz"
tmp_alfabeto = list()

for char in alfabeto:
    tmp_alfabeto.append(char)

alfabeto = tmp_alfabeto
configuracao = list()

for char in alfabeto:
    configuracao.append(char)

texto = str(input("Digite o texto a ser decriptado: "))

def pegar_indice_alfabeto(char):
    return configuracao.index(char)

texto = texto.split(' ')
indice = 0

def testar_configuracao():
    palavras_decriptadas = []
    for palavra in texto:
        nova_palavra = ''
        for letra in palavra:
            nova_palavra += alfabeto[pegar_indice_alfabeto(letra)].lower()
        print(nova_palavra)
        if not nova_palavra in palavras:
            return False
        palavras_decriptadas.append(nova_palavra)
    return palavras_decriptadas

while True:
    random.shuffle(configuracao)
    #configuracao = ['z', 'w', 'f', 'u', 'j', 'k', 'e', 'q', 'i', 'a', 'h', 'l', 'c', 'v', 'o', 'g', 'r', 'm', 'b', 's', 'n', 'x', 'y', 't', 'd', 'p']
    if testar_configuracao():
        print(f"[+] {configuracao} {testar_configuracao()}")
        break
