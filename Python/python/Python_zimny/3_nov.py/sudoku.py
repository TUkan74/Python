sudoku = [""]*9

for i in range(0, 9):
    sudoku[i] = input()
    '''cislo = input()
    for j in range(0, 9):
        sudoku[i][j] = cislo[j]'''

je = True

if je != False:

    for i in range(0, 9):
        riadky = set()
        for j in range(0, 9):
            if sudoku[i][j] in riadky and je == True:
                print("ne, chyba v radku", i)
                je = False
                break
            if sudoku[i][j] not in riadky:
                riadky.add(sudoku[i][j])

    if je == True:
        for i in range(0, 9):
            stlpce = set()
            for j in range(0, 9):

                if sudoku[j][i] in stlpce and je == True:
                    print("ne, chyba ve sloupci", i)
                    je = False
                    break
                if sudoku[j][i] not in stlpce:
                    stlpce.add(sudoku[j][i])


if je != False:
    for l in range(0, 9, 3):
        for i in range(0, 9, 3):
            stvorec = set()
            if je == False:
                break
            for k in range(l, l+3):
                for j in range(i, i+3):
                    stvorec.add(sudoku[k][j])
                    if je == False:
                        break
            if len(stvorec) != 9:
                print("ne, chyba ve ctverci", l, i)
                je = False
                break


if je != False:
    print("ano")
