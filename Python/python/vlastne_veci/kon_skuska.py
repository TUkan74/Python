M, N, y, x = [int(i) for i in input().strip().split()]

sachovnica = [ [False for _ in range(M)] for _ in range(N)]
x-=1
y-=1
sachovnica[x][y] = True

move_x = [-1, -2, -2, -1, 1, 2, 2, 1]
move_y = [-2, -1, 1, 2, 2, 1, -1, -2]




def is_valid(x,y):
    
    suradnice = []
    
    for i in range(8):
        posun_x = x + move_x[i]
        posun_y = y + move_y[i]
        if 0<= posun_x < N and 0<= posun_y < M: 
            if sachovnica[posun_x][posun_y] is False:
                suradnice.append((posun_x,posun_y))

    return suradnice    

def Cesta(Suradnice : list, sucet : int):

    if sucet == 0:
        return "ANO"
    
    for skok in Suradnice:
        x = skok[0]
        y = skok[1]
        sachovnica[x][y] = True 
        vysledok = Cesta(is_valid(x,y),sucet - 1)
        if vysledok is not None:
            return vysledok
        sachovnica[x][y] = False

vysledok = Cesta(is_valid(x,y), N * M -1)

if vysledok is None:
    print("NE")
else:
    print("ANO")
    


