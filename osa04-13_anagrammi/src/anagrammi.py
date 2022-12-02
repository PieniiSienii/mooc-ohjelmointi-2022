def anagrammi(mjono,mjono2):
    if sorted(mjono) == sorted(mjono2):
        return True
    else:
        return False
if __name__ =="__main__":
    print(anagrammi("a","a"))