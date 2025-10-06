import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100) # randint(a, b) retorna um inteiro N tal que a <= N <= b
    tentativas = 0
    
    print("Você tem que adivinhar o número entre 1 e 100!")
    
    while True:
        palpite = input("Qual é o seu palpite? ").strip() # strip() remove espaços em branco no início e no fim
        
        if not palpite.isdigit(): # isdigit() verifica se a string é composta apenas por dígitos
            print("Por favor, insira um número válido.")
            continue
        
        palpite = int(palpite)
        tentativas += 1
        
        if palpite < numero_secreto:
            print("Chutou baixo! Tente um número maior.")
        elif palpite > numero_secreto:
            print("Chutou alto! Tente um número menor.")
        else:
            print(f"Acertou! O número era {numero_secreto}. Você fez {tentativas} tentativas.")
            break

jogo_adivinhacao()
