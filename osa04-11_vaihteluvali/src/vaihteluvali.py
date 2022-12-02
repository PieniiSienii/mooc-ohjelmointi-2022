def vaihteluvali(lista: list):
    palautus = sorted(lista)[len(lista)-1] - sorted(lista)[0]
    return palautus
if __name__ == "__main__":
    lista = [1, 2, 3, 4, 5] 
    tulos = vaihteluvali(lista) 
    print(tulos)