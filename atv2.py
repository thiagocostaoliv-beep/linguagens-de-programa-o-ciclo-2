import math

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

if a >= b and a >= c:
    maior = a
    x = b
    y = c
elif b >= a and b >= c:
    maior = b
    x = a
    y = c
else:
    maior = c
    x = a
    y = b

if maior >= x + y:
    print("Não formam um triângulo.")
    print("Valores informados:", a, b, c)
else:
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))

    print("Formam um triângulo!")
    print(f"Área do triângulo: {area:.2f}")