def palindromi(mjono):
    if mjono == mjono[::-1]:
        return True
    else:
        return False
if __name__ == "__main__":
    print(palindromi("saippuakauppias"))

mjono =input("Anna palindromi: ")
while mjono != mjono[::-1]:
    print("ei ollut palindromi")
    mjono =input("Anna palindromi: ")
print(mjono, "on palindromi!")