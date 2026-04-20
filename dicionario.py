# Criando um dicionario de alunos
"""portal_alunos = {
    "Ana": 9.5,
    "Guilherme": 5,
    "Aurora": 10
}
portal_alunos["Diego"] = 7.6

nome_busca = input("Digite o nome do aluno para ver a nota: \n")

if nome_busca in portal_alunos:
    print(f'A nota de {nome_busca} é {portal_alunos[nome_busca]}.')
else:
    print("Aluno não encontrado!")

notas = portal_alunos.values() #Isso isola apenas as notas
media = sum(notas) / len(portal_alunos)"""

portal_alunos={}

while True:
    print('\n------- PORTAL DO PROFESSOR -------\n')
    print('1.Adicionar Aluno e Nota | 2.Exibir Nota | 3.Sair')
    opcao = input("Digite a opção desejada: ")

    
    if opcao == '1':
        nome=input('Digite o nome do aluno: \n')
        nota = float(input(f'Digite a nota de {nome}:\n'))
        portal_alunos[nome]=nota
    elif opcao == '2':
        nome_busca = input('Digite um nome para consultar:\n')
        if nome_busca in portal_alunos:
            print(f'A nota de {nome_busca} é: {portal_alunos[nome_busca]}')
        else:
            print('Aluno não encontrado')
    elif opcao == '3':
        print('Saindo...\nAté a próxima!')
        break