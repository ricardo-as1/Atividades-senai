numero_str = input("Digite o primeiro número: ") 
numero1 = int(numero_str)
numero_str = input("Digite o segundo número: ")
numero2 = int(numero_str)

mensagem = f"O maior número é {numero1}" if numero1 > numero2 else f"O maior número é {numero2}" # Utilização a condição ternária para determinar o maior número
print(mensagem)