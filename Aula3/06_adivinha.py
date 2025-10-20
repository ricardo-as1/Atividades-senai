import random

numero_secreto = random.randint(1, 10)
tentativas = 0

print("Você tem que adivinhar o número secreto entre 1 e 10!")

while True:
  palpite = input("Qual é o seu palpite? ")

  if not palpite.isdigit():
    print("Por favor, insira um número válido.")
    continue

  palpite = int(palpite)
  tentativas += 1

  if palpite < numero_secreto:
    print("Chutou baixo! Tente um número maior.")
  elif palpite > numero_secreto:
    print("Chutou alto! Tente um número menor.")
  else:
    print(f"Acertou! O número era {numero_secreto}. Você fez {tentativas} tentivas.")
    break