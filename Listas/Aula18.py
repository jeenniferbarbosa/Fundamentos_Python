# teste = list()
# teste.append("Jennifer")
# teste.append(20)
# galera = list()
# galera.append(teste[:])
# # Para add outros elementos na lista é necessário fazer uma cópia
# teste[0] = "Maria"
# teste[1] = 45
# galera.append(teste[:])
# print(galera)

# galera = [["Joao", 19], ["Jennifer", 20], ["Warlley", 14], ["Josi", 34]]
# print(galera[0][0], galera [2][1])
#
# for pessoa in galera:
#     print(f"{pessoa[0]} tem {pessoa[1]} anos de idade")

galera = list()
dado = list()
total_menor = total_maior = 0

for cont in range(0,3):
    dado.append(str(input("Nome: ")))
    dado.append(int(input("Idade: ")))
    galera.append(dado[:]) # **cópia de dados
    dado.clear()

for pessoa in galera:
    if pessoa[1] >= 21:
        print(f"{pessoa[0]} é maior de idade.")
        total_maior += 1
    else:
        print((f"{pessoa[0]} é menor de idade."))
        total_menor += 1

print(f"Temos {total_maior} pessoas maiores de idade e {total_menor} menor de idade.")