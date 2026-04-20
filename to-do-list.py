minhas_tarefas=[]


while True: #Com o while TRUE, ele sempre volta para o while, só se encerra no break
    print('--------- GERENCIADOR DE TAREFAS ---------\n')
    print('1.Aidiconar | 2.Listar | 3.Remover | 4.Sair')
    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        nova = input("Digite a tarefa: ").strip().lower()#insira a tarefe em uma variavel dentro do loop. strip() remove os espaços extras e lower() transforma tudo em minusculo
        minhas_tarefas.append(nova)#adicione a variavel na lista
    
    elif opcao =='2':
        print('Sua Lista: \n')
        for tarefa in minhas_tarefas:
            print(f"- {tarefa.capitalize()}")#capitalize() deixa a primeira letra em maiusculo ao exibir

    elif opcao == '3':
        alvo = input('Qual tarefa deseja remover?').lower()#cria a variavel local para escolher a tarefa a ser excluida

        if alvo in minhas_tarefas: #se o objeto de digitação estiver na lista, ele remove usando a variavel de parametro
            minhas_tarefas.remove(alvo)#seleciona a lista, aplica a função defindo o parametro
            print(f'Tarefa {alvo} removida com sucesso!')
        else:
            print('ERRO! Essa tarefa não está na lista')
    elif opcao == '4':
        print('Saindo... \nAté logo!')
        break #Quando é digitada a opcao 3, o break encerra o while imediatamente
