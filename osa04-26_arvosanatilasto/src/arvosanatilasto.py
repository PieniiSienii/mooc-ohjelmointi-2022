while True:
    pisteiden_maara = (input("Koepisteet ja harjoitusten määrä: "))
    valilyonti = pisteiden_maara.split(" ")
    koepisteet = int(valilyonti[0])
    print(koepisteet)
    harjoitusten_maara = int(valilyonti[1])
    print(harjoitusten_maara)
    if 9 < harjoitusten_maara < 20:
        harjoitusten_pisteet = 1
    elif 19 < harjoitusten_maara < 29:
        harjoitusten_pisteet = 2
    elif 29 < harjoitusten_maara < 39:
        harjoitusten_pisteet = 3
    elif 39 < harjoitusten_maara < 49:
        harjoitusten_pisteet = 4
    elif 49 < harjoitusten_maara < 59:
        harjoitusten_pisteet = 5
    elif 59 < harjoitusten_maara < 69:
        harjoitusten_pisteet = 6
    elif 69 < harjoitusten_maara < 79:
        harjoitusten_pisteet = 7
    elif 79 < harjoitusten_maara < 89:
        harjoitusten_pisteet = 8
    elif 89 < harjoitusten_maara < 99:
        harjoitusten_pisteet = 9
    elif harjoitusten_maara == 100:
        harjoitusten_pisteet = 10
    else:
        harjoitusten_pisteet = 0
    kokonais_pisteet = koepisteet + harjoitusten_pisteet
    print(kokonais_pisteet)
    if pisteiden_maara == "":
        break
