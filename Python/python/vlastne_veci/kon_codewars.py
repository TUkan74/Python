def knight(p1, p2):

    wh = set()
    source = ord(p1[0])-96, int(p1[1]), 0
    dest = ord(p2[0])-96, int(p2[1])
    Queue = []
    Queue.append(source)
    x = 0
    y = 1
    vysledok = 0
    pohyb = [
        ( 1, 2),
        ( 1,-2),
        ( 2, 1),
        ( 2,-1),
        (-1, 2),
        (-1,-2),
        (-2,-1),
        (-2, 1)
    ]
    for i in range(2):
        if source[i] < 1 or source[i] > 8:
            return 0
    for i in range(2):
        if dest[i] < 1 or dest[i] > 8:
            return 0

    def is_valid(x):
        if (x[0] >= 1 and x[1] <= 8 and x[0] <= 8 and x[1] >= 1) :
            
            return True
        else:
            return False

    while Queue:
        suradnice = Queue.pop(0)

        # Finished?
        if suradnice[x] == dest[x] and suradnice[y] == dest[y]:
            return suradnice[2]

        else:

            

            # horse moves
            surx = suradnice[x]
            sury = suradnice[y]
            poradie = suradnice[2]

            # All possible positions
            for i in range(len(pohyb)):

                posun = surx+pohyb[i][0], sury+pohyb[i][1], poradie+1

                if is_valid(posun):
                    Queue.append(posun)

    return poradie

print(knight("a1","c2"))