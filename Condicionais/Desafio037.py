num = int(input("Digite um número: "))
opcao = str(input(""" 
Escolha uma base para conversão: 
Conversão para binário - [1]
Conversão para octal - [2]
Conversão para hexadecimal - [3]
Digite a opção desejada: """))

print(' ')

if opcao == "1":
    print(f"O número {num} em base binário é {bin(num)[2:]}.")
elif opcao == "2":
    print(f"O número {num} em base binário é {oct(num)[2:]}.")
elif opcao == "3":
    print(f"O número {num} em base binário é {hex(num)[2:]}.")
else:
    print("Opção inválida! Tente novamente.")