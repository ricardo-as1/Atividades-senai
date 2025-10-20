while True:
  entrada = input("Digite um número(negativo para sair): ")

  numero = int(entrada)

  if numero < 0:
    print(f"Você digitou um numero negativo, desligando...")
    break