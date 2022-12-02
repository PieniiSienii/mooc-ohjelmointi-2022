sana1 = input("sana: ")
lista = [sana1]
while True:
    sana = input("sana: ")
    if sana in lista:
        break
    lista.append(sana)
print(f"Annoit {len(lista)} eri sanaa")

    

