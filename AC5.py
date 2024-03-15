"""AC5, ao vivo"""

import random
def main():

    vida = 100
    att = (random.randint(10, 20))
    defe = (random.randint(1, 5))

    aventureiro = vida, att, defe

    vidam = (random.randint(60, 80))
    attm = (random.randint(20, 30))

    monstro = vidam, attm

    print("Vida Aventureiro:", vida, "Ataque Aventureiro:", att, "Defesa Aventureiro:", defe)
    print("Vida Monstro:", vidam, "Ataque Monstro:", attm)
    while vida > 0 and vidam > 0:
        vida - (attm - defe) and vidam (vidam - att)
        print("Vida do aventureiro", vida, "Vida do monstro", vidam)

main()
