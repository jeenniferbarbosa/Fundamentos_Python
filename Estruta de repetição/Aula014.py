# While usado quando nao sabemos o limite

# c = 1
# while c < 10:
#     print(c)
#     c = c + 1
# print("FIM")

r = "S"
while r == "S":
    n = int(input("Digite um valor: "))
    r = str(input("Quer continuar? [S/N]: ")).upper()
print("FIM")

# num = 1
# par = 0
# impar = 0
# while num != 0:
#     num = int(input("Digite um valor: "))
#     if num != 0:
#         if num % 2 == 0:
#             par += 1
#         else:
#             impar += 1
# print(f"Voce digitou {par} números pares e {impar} números impares.")
# print("ACABOU")