def positiivisten_summa(lista: list):
    vastaus = 0
    for i in lista:
        if i > 0:
            vastaus += i
    return vastaus

            
if __name__ == "__main__":
    lista = [1, -2, 3, -4, 5]
    vastaus = positiivisten_summa(lista)
    print("vastaus", vastaus)