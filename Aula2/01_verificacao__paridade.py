numero_str = input("Digite um número inteiro: ") # Solicita ao usuário que insira um número inteiro
numero = int(numero_str) # Converte a entrada para um número inteiro

if numero % 2 == 0: # Verifica se o número é divisivel por 2 ou 0
    print(f"O número {numero} é par.")
else: # Caso contrário, o número é ímpar
    print(f"O número {numero} é ímpar.")