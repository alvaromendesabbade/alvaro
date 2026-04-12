nome_do_aparelho = input("Qual aparelho você deseja que seja analisado?: ")
potência_do_aparelho = float(input("Qual a potência deste aparelho em Watts?: "))
tempo_médio_de_uso = float(input("Qual o tempo médio de uso deste aparelho diariamente em horas?: "))
mês = 30
fator_de_conversão_de_Watts_para_Kilowatts = 1000
consumo_mensal = float((potência_do_aparelho * tempo_médio_de_uso * mês)/ fator_de_conversão_de_Watts_para_Kilowatts)
valor_fixo = 0.75 
custo_estimado = consumo_mensal * valor_fixo
print(f"O consumo mensal do {nome_do_aparelho} é de {consumo_mensal} kWh com custo estimado de R${custo_estimado}.")