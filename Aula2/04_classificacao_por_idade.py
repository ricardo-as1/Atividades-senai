numero = input("Digite sua idade: ")
numero = int(numero)

if numero < 18: # se a idade for menor que 18
  print("Você é uma criança.")
elif numero >= 18 and numero < 64: # se a idade for maior que 18 e menor que 64
  print("Você é um adulto.")
else: 
  print("Você é um idoso.") # se a idade for maior ou igual a 64