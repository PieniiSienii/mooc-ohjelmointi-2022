def eka_sana(lause):
        valilyonti = lause.find(" ")
        return lause[0:valilyonti]
    
def toka_sana(lause):
    valilyonti = lause.find(" ") 
    lause = lause[valilyonti + 1:]
    toinen_valilyonti = lause.find(" ")
    if toinen_valilyonti == -1:
        return lause
    return lause[0:toinen_valilyonti]

def vika_sana(lause):
    lause.find(" ")
    while lause.find(" ") != -1:
        lause = lause[lause.find(" ")+1:]
    return lause


if __name__ == "__main__":
    lause = "eka toka"
    print(eka_sana(lause))
    print(toka_sana(lause))
    print(vika_sana(lause))



