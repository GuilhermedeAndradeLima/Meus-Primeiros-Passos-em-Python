import string
import random

letras = string.ascii_letters # "abcdef...XYZ"
numeros = string.digits #"0123456789"
simbolos = string.punctuation # "!"#$%&'..."


#Função Fabrica de senha
def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits #+ string.punctuation
    senha = ""
    for i in range(tamanho):
        senha += random.choice(caracteres)
    return senha

while True:
    try:#Try é um loop de segurança, impedindo que pareça que o programa "quebrou" quando o usuario digitar algo fora do escopo.
        tamanho = int(input('Digite o tamanho que voce deseja sua senha: ')) #Se o usuario digitar um numero, o codigo continua aqui
        qtd = ""
        while True:
            try:
                qtd = int(input('Digite a quantidade de senhas que voce deseja: '))
                print(f'Gerando {qtd} senhas: ')
                for i in range(qtd):
                    nova_senha = gerar_senha(tamanho)
                    print(f'{i+1}ª senha: {nova_senha}')
                    with open("historico_senhas.txt","a") as arquivo:
                        arquivo.write(f"Senha {i+1}: {nova_senha}\n") 
                break
            except:
                print('Ops! Digite um numero inteiro...')

            
        break
    except ValueError:
        print('Ops!. Você precisa digitar um numero inteiro (Ex: 12)')#Se o usuario digitar algo que nao seja um numero, o codigo Python pula pra cá

