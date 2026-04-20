import string
import random

letras = string.ascii_letters # "abcdef...XYZ"
numeros = string.digits #"0123456789"
simbolos = string.punctuation # "!"#$%&'..."


#Função Fabrica de senha
def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ""
    for i in range(tamanho):
        senha += random.choice(caracteres)
    return senha

#print(gerar_senha(8))


qtd = 5
print(f'Gerando {qtd} senhas: ')

for i in range(qtd):
    nova_senha = gerar_senha(12)
    print(f'{i+1}ª senha: {nova_senha}')