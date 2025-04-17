print("˜˜˜˜˜˜˜˜˜˜˜˜˜˜ TABUADA ˜˜˜˜˜˜˜˜˜˜˜˜˜˜")

while True:
    print("------" * 8)
    num = int(input("Informe um número e veja sua tabuada: "))
    print("------" * 8)
    if num < 0:
        break
    for cont in range(0, 11):
        mult = num * cont
        print(f"{num} * {cont} = {mult}")
print("A tabuada foi FINALIZADA! Obrigada por utilizar o programa.")