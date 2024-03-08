def ler_nome():
    """Retorna o nome do aluno inserido pelo usuário."""
    return input("Informe o seu nome: ")
    if ler_nome == _ :
    return False

def ler_notas():
    """Lê as notas de AP1, AP2, AS e AC do aluno, e retorna essas notas."""
    ap1 = float(input("Insira a nota da AP1: "))
    ap2 = float(input("Insira a nota da AP2: "))
    asub = float(input("Insira a nota da AS: "))
    ac = float(input("Insira nota de AC: "))
    return(ap1, ap2, asub, ac)

def analisar_subst(ap1, ap2, asub):
    if asub > ap1:
        return (asub, ap2)
    elif asub > ap2:
        return (ap1, asub)
    else:
        return (ap1, ap2)
    """
    Retorna as duas notas a serem usadas no cálculo.
    A AS deve substituir a AP1 ou AP2 se for maior que elas.
    """

def notas_sao_validas(ap1, ap2, asub, ac):
    if 0 <= ap1 <= 10 and 0 <= ap2 <= 10 and 0 <= asub <= 10 and 0 <= ac <= 10:
        return True
    else: (print("Notas inválidas"))

    """Retorna True se todas as notas estão entre 0 e 10, inclusive."""
    
def calcular_media(ap1, ap2, asub, ac):
    """Calcula e retorna a média final do aluno."""
    prova1, prova2 = analisar_subst(ap1, ap2, asub)
    return (prova1 + prova2) * 0.4 + ac * 0.2

def aluno_foi_aprovado(media):
    """Retorna True se a média foi suficiente para aprovação do aluno."""
    return media >= 7



def main():
    nome = ler_nome()
    if nome:
        ap1, ap2, asub, ac = ler_notas()
        if notas_sao_validas(ap1, ap2, asub, ac):
            media = calcular_media(ap1, ap2, asub, ac)
            if aluno_foi_aprovado(media):
                print("Aluno foi aprovado.")
            else:
                print("Aluno foi reprovado.")

main()
