from random import randint
from time import sleep
from operator import itemgetter

jogadores = {
            "Jogador01": randint(1,6),
            "Jogador02": randint(1,6),
            "Jogador03": randint(1,6),
            "Jogador04": randint(1,6)
}

ranking = list()
print("========= DADOS LANÇADOS =========")
print("Valores sorteados:")

for k, v in jogadores.items():
    print(f"{k} tirou o número: {v}")
    sleep(1)

print("====== RANKING DE CAMPEOES ======")
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True) #Ordena pelo índice 1 e deixa em ordem crescente

for i, v in enumerate(ranking):
    print(f"{i + 1}ª lugar: {v[0]} com {v[1]}")
    sleep(1)