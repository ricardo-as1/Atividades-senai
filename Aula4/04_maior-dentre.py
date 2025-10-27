import random

numeros_aleatorios = []

for _ in range(10):
    numero = random.randint(1, 100)
    numeros_aleatorios.append(numero)

maior_valor = max(numeros_aleatorios)
menor_valor = min(numeros_aleatorios)

print(f"Números aleatórios: {numeros_aleatorios}")
print(f"O maior valor: {maior_valor}")
print(f"O menor valor: {menor_valor}")
