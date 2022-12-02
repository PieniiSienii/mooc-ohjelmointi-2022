luku = int(input("Anna luku: "))
lista = []
while True:
    if luku == 0:
        break
    lista.append(luku)
    print(f"Lista: {lista}")
    print(f"Järjestettynä: {sorted(lista)}")
    luku = int(input("Anna luku: "))
print("Moi!")
