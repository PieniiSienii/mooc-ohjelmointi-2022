def ilman_vokaaleja(mjono:str):
    vokaalit = "aeiouyåäö"
    merkki2 = ""
    for merkki in mjono:
        if merkki not in vokaalit:
            merkki2 += merkki
    return merkki2

if __name__ == "__main__":
    mjono = "abcdefghijklmnopqrstuvwxyzåäö"
    print(ilman_vokaaleja(mjono)) 
