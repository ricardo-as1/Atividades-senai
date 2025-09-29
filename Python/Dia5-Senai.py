# ================== Atividades: 29/09/2025 Senai ==================

#1) - Faça um Programa que peça as 4 notas bimestrais e mostre a média.

"""
nota1 = int(input("Nota do primeiro bimestre: "))
nota2 = int(input("Nota do segundo bimestre: "))
nota3 = int(input("Nota do terceiro bimestre: "))
nota4 = int(input("Nota do quarto bimestre: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

print("A média do aluno no ano é: ", media) """

#2) - Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius. C = (5 * (F-32) / 9).

"""
celsius =  int(input("Digite a temperatura em Celsius: "))

fahrenheit = (celsius *9/5) + 32

print("A temperatura em Fahrenheit é: ", fahrenheit) """

#3 - Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre: o produto do dobro do primeiro com metade do segundo. a soma do triplo do primeiro com o terceiro. o terceiro elevado ao cubo.

"""
numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))
numeroR = float(input("Digite um número real: "))

produto = (numero1 * 2) * (numero2 / 2)
soma = (numero1 * 3) + numeroR
cubo = numeroR ** 3

print("O produto do dobro do primeiro com metade do segundo é: ", produto)
print("A soma do triplo do primeiro com o terceiro é: ", soma)
print("O terceiro elevado ao cubo é: ", cubo) """

#4 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

"""
valorhora = float(input("Quanto você ganha por hora? "))
horastrabalhadas = int(input("Quantas horas você trabalha no mês? "))

salario = valorhora * horastrabalhadas

print("O seu salário no mês é: R$", salario) """

#5 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Com descon

#Salário Bruto : R$
#IR (11%) : R$
#INSS (8%) : R$
#Sindicato ( 5%) : R$ = Salário Liquido : R$ Obs.: Salário Bruto - Descontos = Salário Líquido.

"""
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
print("O seu salário líquido no mês é: R$", salarioliquido) """

# ================== Fim das Atividades ==================