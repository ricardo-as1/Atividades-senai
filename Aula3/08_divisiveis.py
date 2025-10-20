quantidade = 0

for i in range(99, 1000):
  if (i % 3 == 0) and (i % 7 == 0):
    print(i)
    quantidade += 1

print(f"Quantidade de números divisíveis por 3 e 7 entre 100 e 999: {quantidade}")