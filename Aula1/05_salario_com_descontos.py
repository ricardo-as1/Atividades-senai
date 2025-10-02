valorhora = float(input("Quanto você ganha por hora? "))
horastrabalhadas = int(input("Quantas horas você trabalha no mês? "))

salario = valorhora * horastrabalhadas
ir = salario * 0.11
inss =  salario * 0.08
sindicato = salario * 0.05
descontos = ir + inss + sindicato
salarioliquido = salario - descontos

print("O seu salário bruto no mês é: R$", salario)
print("O valor do IR (11%) é: R$", ir)
print("O valor do INSS (8%) é: R$", inss)
print("O valor do Sindicato (5%) é: R$", sindicato)
print("O total de descontos é: R$", descontos)
print("O seu salário líquido no mês é: R$", salarioliquido)