nota1 = float(input("Digite a primeira nota do aluno (a): "))
nota2 = float(input("Digite a segunda nota do aluno (a): "))
media = (nota1 + nota2) / 2

print("===== Média Final =====")

if media < 5:
    print(f"A média final foi {media}. O aluno (a) está REPROVADO!")
elif 5 <= media < 7:
    print(f"A média final foi {media}. O aluno (a) está de RECUPERAÇAO!")
else:
    print(f"A média final foi {media}. O aluno (a) está APROVADO!")