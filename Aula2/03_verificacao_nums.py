numero = input("Digite um número: ")
numero = int(numero)

if numero > 0: # se o numero for maior que 0
  print(f"O número {numero} é positivo.")
elif numero < 0: # se o numero for menor que 0
  print(f"O número {numero} é negativo.")
else: # numero == 0
  print("O número é zero.")