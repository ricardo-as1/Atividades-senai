numero = input("Digite a nota do aluno: ")
numero = float(numero)

if numero == 100: # se a nota for igual a 100
  print("Nem usou chat não.")
elif numero >= 70 and numero < 100: # se a nota for maior ou igual a 70 e menor que 100
  print("Usou metade do chat.")
elif numero == 50 and numero < 70: # se a nota for maior ou igual a 50 e menor que 70
  print("Quase em, da proxima pede pro chat humanizar.")
else: # se a nota for menor que 50
  print("PÉSSIMO, nem o chat te salva.")