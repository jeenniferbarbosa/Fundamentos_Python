## GAME: Pedra Papel e Tesoura

from random import randint
from time import sleep

opcoes = ["Pedra", "Papel", "Tesoura"]
pc = opcoes[randint(0, 2)].lower()
print("""Suas opções: 
- Pedro
- Papel
- Tesoura """)
jogador = str(input("Opção escolhida: ")).lower()
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!")
sleep(1)

print( '=' * 27)
print(f"Computador jogou: {pc}")
print(f"Jogador jogou: {jogador}")
print( '=' * 27)

if pc == jogador:
    print("EMPATE")
elif pc == "pedra" and jogador == "tesoura" or pc == "tesoura" and jogador == "papel" or pc == "papel" and jogador == "pedra" :
    print("O PC VENCEU!")
elif jogador == "pedra" and pc == "tesoura" or jogador == "tesoura" and pc == "papel" or jogador == "papel" and pc == "pedra":
    print("O Jogador VENCEU!")
else:
    print("Jogada inválida! Tente novamente.")