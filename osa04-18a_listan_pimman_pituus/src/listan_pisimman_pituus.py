def pisimman_pituus(lista: list):
    paras = 1
    arvo = 0
    while arvo <= len(lista):
        for alkio in range(len(lista)):
            if len(lista[alkio]) > paras:
                paras = len(lista[alkio])
        return paras


if __name__ == "__main__":
    lista = ["pekka", "emilia", "venla", "eero", "antti", "juhani"]
    tulos = pisimman_pituus(lista)
    print(tulos)