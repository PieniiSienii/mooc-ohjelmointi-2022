def poista_isot(lista: list):
    karsittu_lista = []
    for mjono in lista:
        if mjono.isupper() == False:
            karsittu_lista.append(mjono)
    return karsittu_lista

if __name__ == "__main__":
    lista = ["ABC", "def", "ISO", "TOINENISO", "pieni", "toinen pieni", "Osittain Iso"]
    karsittu_lista = poista_isot(lista)
    print(karsittu_lista)
