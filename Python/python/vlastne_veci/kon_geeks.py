M,N,x,y = [int(i) for i in input().strip().split() ]

Sachovnica = [[False for _ in range(M)]for _ in range(N)]

x-=1
y-=1

move_x = [-2,-2,2,2,-1,-1,1,1]
move_y = [-1,1,1,-1,2,-2,2,-2]


def is_valid(A,B):
    options = []

    for i in range(8):
        x = A + move_x[i]
        y = B + move_y[i]

        if 0<= x < N and 0<= y < M:
            if Sachovnica[x][y] == False:
                options.append((x,y))
    return options

def Cesta(suradnice:list,sucet :int):

    if sucet == 0:
        return "ANO"
    
    for sur in suradnice:
        x = sur[0]
        y = sur[1]
        Sachovnica[x][y] = True
        vysledok = Cesta(is_valid(x,y),sucet-1)
        if vysledok is not None:
            return vysledok
        Sachovnica[x][y] = False

vysledok = Cesta(is_valid(x,y),N*M-1)

if not vysledok:
    print("NE")

else:
    print("ANO")