
nome_usuario = input("Qual seu nome? \n")
idade_usuario=int(input("Qual é a sua idade? \n"))#para converter str to int, coloque o input entre paretese
# ... (suas condições de nome e idade aqui)

if idade_usuario >= 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")

continuar = True #Sempre defina a condição verdadeira antes para poder entrar no while

while continuar == True:
    resp_felic = input("Você está feliz hoje? (Sim/Não)\n")

    if resp_felic == 'Sim':
        print("Que bom! Fico feliz por você")
    elif resp_felic == 'Não':
        print("Que pena. Espero que fique bem")
    else:
        print("Resposta inválida")

    
    resposta = input("Quer continuar conversando? (Sim/Não): ") # Esta parte PRECISA estar dentro do while para ser perguntada a cada volta
    
    if resposta == "Não":
        continuar = False #Quando a condição se torna falsa, o programa sai do loop
        print("Até a próxima!")