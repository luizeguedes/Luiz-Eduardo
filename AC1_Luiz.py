# Pedido 1#

a = float(input("Insira a:"))
b = float(input("Insira b:"))
c = float(input("Insira c:"))

delta = b ** 2 - 4 * a * c

raizpositiva = (-1 * b + delta ** 0.5) / (2 * a)
raiznegativa = (-1 * b - delta ** 0.5) / (2 * a)

print(raizpositiva, raiznegativa)

print(30 * "---")

# Pedido 2 #

ano = int(input("Insira Ano "))

ano = ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0



