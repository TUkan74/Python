sx,sy,ex,ey = [int(i) for i in input().strip().split()]

sachovnica = [[False for _ in range(8)]for _ in range(8)]
N = 8
sx-=1
sy-=1
ey-=1
ex-=1

Q = []
Q.append((sx,sy,0))
sachovnica[sx][sy] = 0
move_x = [-1, -2, -2, -1, 1, 2, 2, 1]
move_y = [-2, -1, 1, 2, 2, 1, -1, -2]


def is_valid(suradnice):
    x= suradnice[0]
    y= suradnice[1]
    poradi = suradnice[2]

    if 0 <= x < N and 0 <= y < N:
        if sachovnica[x][y] == False:
            sachovnica[x][y] = poradi
        return True
    else: 
        return False

def kon(ex,ey):
    poradie = 0
    while Q:
        posun = Q.pop(0)
        poradie = posun[2]
        if posun[0] == ex and posun[1] == ey:
            return posun[2]

        for i in range(8):
            skok = (posun[0]+move_x[i], posun[1]+move_y[i],poradie+1)
            if is_valid(skok):
                Q.append(skok)
        
    
    return False

print(kon(ex,ey))