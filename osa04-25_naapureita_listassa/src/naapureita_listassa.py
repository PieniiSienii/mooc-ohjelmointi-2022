def pisin_naapurijono(lista: int):
    pisin = 1
    tulos = 1
    seuraava_numero = 1
    for numero in lista:
        if seuraava_numero <= len(lista)-1:
            if lista[seuraava_numero] - numero == 1 or numero - lista[seuraava_numero] == 1 :
                tulos += 1
                if tulos > pisin:
                    pisin = tulos
            elif lista[seuraava_numero] - numero != 1:
                tulos = 1
            seuraava_numero += 1
    return pisin
        







if __name__ == "__main__":
    lista = [1, 2, 3, 5, 6, 9, 10]
    print(pisin_naapurijono(lista))