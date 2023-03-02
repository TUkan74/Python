
# velkost sachovnice ROZMER x ROZMER
ROZMER = 8

def je_na_sachovnici(pole):
    return 0 <= pole[0] < ROZMER and 0 <= pole[1] < ROZMER

def precti_sachovnici():
    print('Zadej sachovnici (. je volne policko, X je obsazene policko, K je kral)')
    kral = None
    sachovnice = []
    for x in range(ROZMER):
        radek = input().strip()
        sachovnice.append(list(radek))
        if radek.find('K') >= 0:
            if kral == None:
                kral = (x,radek.index('K'))
            else:
                print('Chyba, vice kralu na sachovnici')
                exit()
    if not kral:
        print('Chybi kral')
        exit()
    return sachovnice, kral


def je_cesta(kral, cil, sachovnice):
    # rekurzivne
    pass

def je_cesta(kral, cil, sachovnice):
    wh = set()
    pohyb = [( 1, 1),
             ( 0, 1),
             (-1, 1),
             (-1, 0),
             (-1,-1),
             ( 0,-1),
             ( 1,-1),
             ( 1, 0)]
    Queue = []
    Queue.append(kral)
    wh.add(kral)
    buduci = (0,0)
    x= 0
    y = 1
    while Queue:
        pozicia = Queue.pop(0)
        if pozicia[x] == cil[x] and pozicia[y] == cil[y]:
            return True
        for i in pohyb:
            
            
            buduci[x] = pozicia[x] + pohyb[i][y]
            buduci[y] = pozicia[y] + pohyb[i][x]



            if buduci not in wh:
                wh.add(buduci)
                Queue.append(buduci)
    return False         
    pass



def najdi_cestu(kral, cil, sachovnice):
    # rekurzivne
    pass
 
def najdi_cestu(kral, cil, sachovnice):
    # bez rekurze
    pass
 

sachovnice, kral = precti_sachovnici()
cil = [i for i in input('Zadej cilove policko: ').split()]
if je_cesta(kral, cil, sachovnice):
    print('Cesta existuje')
else:
    print('Cesta neexistuje')