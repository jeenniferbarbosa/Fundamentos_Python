from random import randint
from time import sleep

pc = randint(0, 5)
print("Vou pensar em um número de 0 a 5. Tente adivinhar.")
jogador = int(input("Em que número eu pensei? "))
print("Processando...")
sleep(2)

if jogador == pc:
    print("Parabéns você acertou!!")
else:
    print(f"Que pena, você errou! Eu pensei no número {pc}.")