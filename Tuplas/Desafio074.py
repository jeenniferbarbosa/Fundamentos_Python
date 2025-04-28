from random import randint

num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f"Os númertos sorteados foram: ", end="")
for cont in num:
    print(f"{cont}", end=" ")
print(f"\nO maior número sorteado foi {max(num)}")
print(f"O menor número sorteado foi {min(num)}")