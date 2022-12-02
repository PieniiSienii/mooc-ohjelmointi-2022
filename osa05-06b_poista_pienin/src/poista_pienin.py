def poista_pienin(luvut: list):
    pienin = luvut[0]
    for alkio in luvut:
        if alkio <= pienin:
            pienin = alkio
    luvut.remove(pienin)


if __name__ == "__main__":
    luvut =[1, 2, 3, 5, 6]
    poista_pienin(luvut)
    print(luvut)