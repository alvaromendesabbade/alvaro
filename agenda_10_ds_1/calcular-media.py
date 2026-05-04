def calcular_media(notas):
    tamanho=len(notas)
    totalnota=0
    j=0
    while j < tamanho:
        totalnota=totalnota+notas[j]
        j=j+1
    media=totalnota/tamanho
    return media

def verificar_aprovacao(media):
    if media >= 6:
        return "Aprovado(a)"
    else:
        return "Reprovado(a)"


print ("Olá, seja bem-vindo(a) ao sistema de cálculo de notas dos alunos!")
nome=input("Insira o nome do aluno que será avaliado: ")
quantidade=int(input("Quantas notas serão inseridas?: "))
notas=[]
i=0
while i < quantidade:
    nota=float(input(f"Insira a nota {i}: "))
    notas.append(nota)
    i=i+1

media=calcular_media(notas)
status_aprovacao=verificar_aprovacao(media)
print (f"O(a) aluno(a) {nome}  foi {status_aprovacao}")