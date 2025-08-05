from random import sample
from time import sleep

print("==" * 8, "MEGA SENA", "=" * 15)

num_sorte = list()
num_jogos = int(input("Quantos palpites gostaria de criar? "))

print("---" * 14)

for c in range(0, num_jogos):
    num_sorte.append(sample(range(1, 61), 6))

for i, palpites in enumerate(num_sorte, start=1):
    sleep(1)
    print(f"{i}ª palpite: {sorted(palpites)}")

print(' ')
sleep(1)
print("BOA SORTE!!")
