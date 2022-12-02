
def pisimmat(lista: list):
    paras = 0
    uusi_lista = []
    tulostettava_lista = []
    for alkio in lista:
        if len(alkio) >= paras:
            paras = len(alkio)
            paras_nimi = alkio
            uusi_lista.append(paras_nimi)
    for alkio in uusi_lista:
        if len(alkio) == len(paras_nimi):
            tulostettava_lista.append(alkio)
    return tulostettava_lista


if __name__ == "__main__":
    lista = ["arto", "leena", "johanna", "venla", "santeri", "antti"]
    tulos = pisimmat(lista)
    print(tulos)
