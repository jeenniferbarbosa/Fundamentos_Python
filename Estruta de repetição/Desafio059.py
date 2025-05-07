from time import sleep

while True:
    num1 = int(input("Informe o primeiro número: "))
    num2 = int(input("Informe o segundo número: "))
    opcao = int(input("""Opções: 
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
Digite sua opção: """))

    if opcao == 1:
        soma = num1 + num2
        print(f"O resultado de {num1} + {num2} é {soma}.")
        print("+=" * 20)
    if opcao == 2:
        mult = num1 * num2
        print(f"O resultado de {num1} * {num2} é {mult}.")
        print("+=" * 20)
    if opcao == 3:
        if num2 > num1:
            print(f"O maior número entre {num1} e {num2} é {num2}.")
        elif num1 > num2:
            print(f"O maior número entre {num1} e {num2} é {num1}.")
    print("+=" * 20)

    if opcao == 4:
        continue
    if opcao == 5:
        print("O programa está sendo finalizado...")
        print("+=" * 20)
        sleep(1.5)
        print("Finalizado. Obrigado por utilizar nosso programa!")
        break
    else:
        print("Opção inválida. Tente novamente...")