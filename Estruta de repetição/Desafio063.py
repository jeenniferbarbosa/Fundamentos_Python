print("========== Sequência de Fibonacci ===========")

n = int(input("Quantos termos da sequência você quer ver? "))
termo1 = 0
termo2 = 1
cont = 3

print(f"{termo1}, {termo2}", end=" >> ")

while cont <= n:
    termo3 = termo1 + termo2
    print(f"{termo3}", end=" >> ")
    termo1 = termo2
    termo2 = termo3
    cont += 1

print("Fim do programa.")