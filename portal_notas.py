portal_alunos={}

while True:
    print('\n------- PORTAL DO PROFESSOR -------\n')
    print('1.Adicionar Aluno e Nota | 2.Exibir Nota | 3.Sair')
    opcao = input("Digite a opção desejada: ")

    
    if opcao == '1':
        nome=input('Digite o nome do aluno: \n')
        while True:
            try:
                nota = float(input(f'Digite a nota de {nome}:\n'))
                portal_alunos[nome]=nota
                
                # --- O BLOCO DE SALVAMENTO ENTRA AQUI ---
                with open("portal_notas.txt", "a") as arquivo:
                    arquivo.write(f"{nome}: {nota}\n")
                # ----------------------------------------

                break
            except ValueError:
                print('ERRO! Digite somente numeros em algarismo: ')
            
    elif opcao == '2':
        nome_busca = input('Digite um nome para consultar:\n')
        if nome_busca in portal_alunos:
            print(f'A nota de {nome_busca} é: {portal_alunos[nome_busca]}')
        else:
            print('Aluno não encontrado')
    elif opcao == '3':
        print('Saindo...\nAté a próxima!')
        break
