num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ")

if operacao == "+":
    resultado = num1 + num2
    print(f"O resultado de {num1} + {num2} é {resultado}")
elif operacao == "-":
    resultado = num1 - num2
    print(f"O resultado de {num1} - {num2} é {resultado}")
elif operacao == "*":
    resultado = num1 * num2
    print(f"O resultado de {num1} * {num2} é {resultado}")
elif operacao == "/":
    if num2 != 0: # Verifica se o divisor não é zero
        resultado = num1 / num2
        print(f"O resultado de {num1} / {num2} é {resultado}")
    else:
        print("Erro: Divisão por zero não é permitida.") # Mensagem de erro para divisão por zero
        