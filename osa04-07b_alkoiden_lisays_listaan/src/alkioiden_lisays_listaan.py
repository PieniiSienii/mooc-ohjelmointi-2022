lista = []
lukujen_maara = int(input("Kuinka monta lukua: "))
while lukujen_maara > 0:
    luku = 1
    anna_luku = int(input(f"Anna luku{luku}: "))
    lista.append(anna_luku)
    luku += 1
    lukujen_maara -= 1
print(lista)
