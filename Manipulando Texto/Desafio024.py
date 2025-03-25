city = str(input("Em qual cidade você nasceu? "))[:5].upper().strip()

if city == "SANTO":
    print(True)
else:
    print(False)