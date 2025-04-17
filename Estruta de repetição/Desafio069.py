## Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. Sem final, mais:
# A) quantas pessoas têm mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres têm menos de 20 anos.

cont = 0
masculino = 0
idade_feminino = 0

while True:
    print("------------------" * 2)
    print("       CADASTRO DE PESSOAS        ")
    print("------------------" * 2)
    nome = str(input("Informe o nome: "))
    idade = int(input("Informe a idade: "))
    gen_sexual = str(input("Informe o genêro sexual [F/M]: ")).upper().strip()
    while gen_sexual != "M" and gen_sexual != "F":
        gen_sexual = str(input("Informe o genêro sexual [F/M]: ")).upper().strip()
    opcao = str(input("Gostaria de continuar [S/N]? ")).upper().strip()
    while opcao != "N" and opcao != "S":
        opcao = str(input("Gostaria de continuar [S/N]? ")).upper().strip()
    if opcao == "N":
        break
    if gen_sexual == "M" or gen_sexual == "m":
        masculino += 1
    if idade >= 18:
        cont += 1
    if (gen_sexual == "F" or gen_sexual == "f") and idade < 20:
        idade_feminino += 1
print(f"Foram cadastradas {masculino} pessoas do genêro masculino.")
print(f"Foram cadastradas {cont} pessoa(as) com mais de 18 anos.")
print(f"Foram cadastradas {idade_feminino} mulheres com menos de 20 anos.")