numero = input("Digite sua idade: ")
numero = int(numero)

if numero > 18:
  print("Você é maior de idade.")
elif numero < 18 and numero > 12:
  print("Você é um adolescente.")
elif numero <= 12 and numero >= 0:
  print("Você é uma criança.")