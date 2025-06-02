# Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta

expr = str(input("Digite um experssão: "))
pilha = list()

for parent in expr:
    if parent == "(":
        pilha.append(parent)
    elif parent in ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            break

else:
    if len(pilha) == 0:
        print("Sua expressão está válida.")
    else:
        print("Sua expressão está errada.")