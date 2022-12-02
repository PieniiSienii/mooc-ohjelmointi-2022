def lyhin(lista: list):
    paras = len(lista[0])
  
    for alkio in lista:
        if len(alkio) <= paras:
            paras = len(alkio)
            paras_nimi = alkio
    return paras_nimi


if __name__ == "__main__":
    lista = ["pekka", "emilia", "johanna", "venla", "eero", "antti"]
    tulos = lyhin(lista)
    print(tulos)
