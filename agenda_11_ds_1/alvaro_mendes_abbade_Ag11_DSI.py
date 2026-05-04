from colorama import Fore, Style 



def situacao_do_reservatorio(n):
    if n == 1:
         print(Fore.RED + "Muito baixo(crítico)!")
    elif n == 2:
        print(Fore.YELLOW +"Baixo")
    elif n == 3:
        print(Fore.GREEN +"Médio")
    elif n == 4:
         print(Fore.CYAN +"Alto")
    elif n == 5:
         print(Fore.BLUE +"Muito Alto (alerta)!")
    else:
        print("Nível invalido! Digite um número de 1 a 5.")
    
print(Style.RESET_ALL) 

nivel = int(input("Qual o nível do reservatório de água (1 a 5)?: "))

situacao_do_reservatorio(nivel)







