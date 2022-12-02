def muotoile(lista: list):
    uusi_lista =[]
    for luku in lista:
        luku =f"{luku:.2f}"
        uusi_lista.append(luku)
    return uusi_lista

if __name__ == "__main__":
    lista = [1.234, 0.3333, 0.11111, 3.446]
    uusi_lista = muotoile(lista)
    print(uusi_lista)