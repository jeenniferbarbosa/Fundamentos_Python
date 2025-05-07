# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

palpites = 0
pc = randint(0, 10)

print("Vou pensar em um número de 0 a 10. Tente adivinhar.")

while True:
    jogador = int(input("Em que número eu pensei? "))
    palpites += 1

    if jogador == pc:
        print(f"Parabéns, você acertou! Seus palpites até o acerto foram {palpites}")
    else:
        if jogador < pc:
            print("É um número maior... Tente novamente.")
        if jogador > pc:
            print("É um número menor... Tente novamente. ")