def uniikit(lista):
    uusi_lista = []
    lista.sort()
    for i in range(len(lista)):
        if lista[i] not in uusi_lista:
            uusi_lista.append(lista[i])
    return uusi_lista



if __name__ == "__main__":
    lista = [3, 2, 2, 1, 3, 3, 1]
    print(uniikit(lista))