def soma(a,b):
    return a + b
def subtracao(a,b):
    return a - b
def multipicação(a,b):
    return a*b
def divisão(a,b):
    if b == 0:
        return("Digite um valor diferente de 0 para o denominador")
    else:
        return a/b

while True:
    print('\n---------CALCULADORA---------\n')
    print('1.Somar | 2.Subtrair | 3.Multiplicar | 4.Dividir | 5.Sair')

    escolha = input("\nEscolha uma opcao: ")

    if escolha == '5':
        print("\nSaindo...\nAté a próxima!")
        break #O comando 'break' interrompe o while na hora!    
    
    if escolha in ['1','2','3','4']:#O programa só permite o input dos numeros se a escolha estiver entre as opções válidas.
        num1=float(input("Digite o 1º número: "))
        num2=float(input("Digite o 2º número: "))

    if escolha == '1':
        print(f'\n\bResultado: {soma(num1,num2)}')
    elif escolha == '2':
        print(f'Resultado: {subtracao(num1,num2)}')
    elif escolha == '3':
        print(f'Resultado: {multipicação(num1,num2)}')
    elif escolha == '4':
        print(f'Resultado: {divisão(num1,num2)}') 
    else:
        print('Opção inválida!')