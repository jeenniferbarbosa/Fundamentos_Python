num = cont = 0
while True:
    num = int(input("Digite um número: "))
    if num == 999:
        break
    cont += num
print(f"A soma vale {cont}")