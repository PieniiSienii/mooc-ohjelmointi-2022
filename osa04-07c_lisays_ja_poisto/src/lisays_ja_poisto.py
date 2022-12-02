lista = []
print("Lista on nyt []")
numero = 1
while True:
    lisaa_vai_poista = input("(l)isää, (p)oista vai e(x)it: ")
    if lisaa_vai_poista == "l":
        lista.insert(len(lista), numero)
        print(f"Lista on nyt {lista}")
        numero += 1
    elif lisaa_vai_poista == "p":
        lista.pop(len(lista)-1)
        print(f"Lista on nyt {lista}")
        numero -= 1
    elif lisaa_vai_poista == "x":
        break
print("Moi!")
