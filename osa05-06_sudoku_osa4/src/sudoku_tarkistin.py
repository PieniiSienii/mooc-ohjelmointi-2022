def rivi_oikein(sudoku: list, rivi_nro: int):
    huomatut_solut = []
    rivi = sudoku[rivi_nro]
    for solu in rivi:
        if solu in huomatut_solut and solu != 0:
            return False
        huomatut_solut.append(solu)
    return True


def sarake_oikein(sudoku: list, sarake_nro: int):
    haetut_luvut = []
    for rivi in sudoku:
      if rivi[sarake_nro] > 0 and rivi[sarake_nro] in haetut_luvut:

        return False
      haetut_luvut.append(rivi[sarake_nro])
    return True



def nelio_oikein(sudoku: list, rivi_nro: int, sarake_nro: int):
    listat = []
    for rivi in range(rivi_nro,rivi_nro+3):
        nelio = (sudoku[rivi][sarake_nro:sarake_nro+3])
        for alkio in nelio:
            if alkio > 0 and alkio in listat:
                return False
        
            listat.append(alkio)
    return True
def sudoku_oikein(sudoku: list):
    for rivi_nro in range(0,len(sudoku)):
            if rivi_oikein(sudoku,rivi_nro) == False:
                return False
    for sarake_nro in range(0,len(sudoku)):
            if sarake_oikein(sudoku, sarake_nro) == False:
                return False
    for rivi_nro in range(0,9,3):
         for sarake_nro in range(0,9,3):
            if nelio_oikein(sudoku, rivi_nro, sarake_nro) == False:
                return False

        
    return True
        
            


if __name__ == "__main__":
        sudoku1 = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]


        print(sudoku_oikein(sudoku1))

        sudoku2 = [
  [ 2, 6, 7, 8, 3, 9, 5, 0, 4 ],
  [ 9, 0, 3, 5, 1, 0, 6, 0, 0 ],
  [ 0, 5, 6, 0, 0, 0, 8, 3, 9 ],
  [ 5, 1, 9, 0, 4, 6, 3, 2, 8 ],
  [ 8, 0, 2, 1, 0, 5, 7, 0, 6 ],
  [ 6, 7, 4, 3, 2, 0, 0, 0, 5 ],
  [ 0, 0, 0, 4, 5, 7, 2, 6, 3 ],
  [ 3, 2, 0, 0, 8, 0, 0, 5, 7 ],
  [ 7, 4, 5, 0, 0, 3, 9, 0, 1 ],
        ]

        print(sudoku_oikein(sudoku2))