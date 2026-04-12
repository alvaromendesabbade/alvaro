
nome = []
idade = []
resposta = []
for i in range(49):
    print("Olá. Seja bem-vindo(a) à pesquisa de opinião da TudoWeb! Temos como objetivo reconhecer o seu grau de satisfação com nosso atendimento a fim de melhorá-lo cada vez mais!")
    n = input("Para começarmos a avaliação, é necessário que informe seu nome: ")
    nome.append(n)
    id = int(input(f"{nome[i]}, qual a sua idade?:  "))
    idade.append(id)
    print("Qual sua opinião sobre o atendimento prestado?")
    print("1. Excelente | 2. Bom | 3. Ruim")
    r = int(input("Insira sua resposta aqui: "))
    resposta.append(r)
    if (resposta[i] > 0 and resposta[i] < 4 ):
        print("Sua resposta foi registrada! Muito obrigado por fazer parte de nossa pesquisa de satisfação!")
    else:
        resposta[i] = input("Sua resposta não foi registrada! Por favor, insira uma resposta com um dos seguintes valores: 1 para Excelente | 2 para Bom | 3 para Ruim: ")

excelente=resposta.count(1)
bom=resposta.count(2)
ruim=resposta.count(3)

print (f"Resultado da pesquisa - Excelente: {excelente}, Bom: {bom}, Ruim: {ruim}")