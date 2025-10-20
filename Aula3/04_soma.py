soma = 0
for numero in range(20):
  if numero % 2 == 0: # Verifica se o número é divisivel por 2 ou igual zero
    soma += numero
    print(f"A soma dos números pares entre 0 e 20 é: {soma}")