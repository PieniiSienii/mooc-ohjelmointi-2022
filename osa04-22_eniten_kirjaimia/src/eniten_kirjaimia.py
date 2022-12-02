def eniten_kirjainta(mjono: list):
    paras = 0
    for kirjain in mjono:
        laskettu_maara = mjono.count(kirjain)
        if laskettu_maara > paras:
            paras = laskettu_maara
            paras_kirjain = kirjain
    return paras_kirjain 




if __name__ == "__main__":
    mjono = "abc"
    print(eniten_kirjainta(mjono))