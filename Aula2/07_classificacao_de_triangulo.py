# Solicita o comprimento dos três lados
lado1 = float(input("Digite o comprimento do primeiro lado: "))
lado2 = float(input("Digite o comprimento do segundo lado: "))
lado3 = float(input("Digite o comprimento do terceiro lado: "))

def classificar_triangulo(a, b, c):
    # Se algum lado for menor ou igual a zero, nao é um triangulo valid
    if a <= 0 or b <= 0 or c <= 0:
        return "Inválido (lados devem ser > 0)"
    
    # verifica se os lados podem formar um triangulo
    if a + b <= c or a + c <= b or b + c <= a:
        return "Não forma um triângulo válido"
    
    # Classificacao
    if a == b == c:
        return "Equilátero"
    elif a == b or b == c or a == c:
        return "Isósceles"
    else:
        return "Escaleno"

tipo = classificar_triangulo(lado1, lado2, lado3)
print(f"O triângulo é do tipo: {tipo}")
