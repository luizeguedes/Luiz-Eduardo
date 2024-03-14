"""Exercício 1"""

def eq_seg_grau(a, b, c):
    delta = b ** 2 - 4 * a * c
    return((-b + delta ** 0,5) / 2 * a , (+b + delta ** 0,5))

eq_seg_grau(2, 3, 6)


print(""--"" * 30)

"""Pedido 2"""

ano = int(input("Insira Ano"))

variavel = ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0

if variavel == True:
  print("bissexto")
else:
  print("não é bissexto")

"""Exercício 2"""

def calcula_sal(valor_hora, num_horas):
    total = valor_hora * num_horas
    salario =   total - (total * 0,275)
    return(salario, (total * 0,275))


