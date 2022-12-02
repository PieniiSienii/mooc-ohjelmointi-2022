def  kaikki_vaarinpain(lista: list):
    lista2 =[]
    for mjono in lista:
        mjono = mjono[::-1]
        lista2.insert(0,mjono)
    return lista2





if __name__== "__main__":
    lista = ["Moi", "kaikki", "esimerkki", "vielä yksi"]
    lista2 = kaikki_vaarinpain(lista)
    print(lista2)