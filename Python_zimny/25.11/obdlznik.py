# jednoduche animace
from time import sleep
# kresleni na platno s rozmery sirka a vyska
vyska = 12
sirka = 60
platno = []
# levy dolni roh platna ma souradnice (0,0), pravy horni roh ma souradnice (sirka-1,vyska-1)
# prvni souradnice je horizontalni, druha vertikalni
for i in range(vyska):
    platno.append(['.'] * sirka)


def tisk():
    for i in range(vyska - 1, -1, -1):
        for j in range(sirka):
            print(platno[i][j], end='')
        print('')
    print('=' * sirka)

def vloz_bod(znak, x, y):
    """Nakresli bod x, y, znakem znak"""
    if 0 <= x < sirka and 0 <= y <vyska:
        platno[y][x] = znak

def vymaz(prazdny_znak='.'):
    for i in range(sirka):
        for j in range(vyska):
            platno[j][i] = prazdny_znak


def obdelnik(znak, ld_x, ld_y, sirka, vyska):
    # znak je znak, kterym bude obdelnik vyplneny
    # ld_x je (x)-va souradnice (l)eveho (d)olniho rohu (sloupec)
    # ld_y je (y)-va souradnice (l)eveho (d)olniho rohu (radek)
    # sirka je sirka obdelnika
    # vyska je vyska obdelnika
    #from time import sleep 
    #sleep 0.5 == sekundy
    for i in range(0,vyska,1):
        for j in range(0,sirka,1):
            vloz_bod(znak,j+ld_x,i+ld_y)
        
    

tisk()
obdelnik("A", 1, 1, 5, 5)
obdelnik('B', 50, 4, 5, 8)
tisk()

# naprogramujte serii obrazku, kde se obdelnik A pohybuje doprava
# a zaroven obdelnik B doleva

poc_x_A = 1      # pocatecni x-ova souradnice obdelniku A
poc_y_A = 1      # pocatecni y-ova souradnice obdelniku A
dx_A = 5         # posun obdelniku A v 1 kroku
sirka_A = 5
vyska_A = 5
poc_x_B = 50     # pocatecni x-ova souradnice obdelniku B
poc_y_B = 4      # pocatecni y-ova souradnice obdelniku A
dx_B = -7        # posun obdelniku B v 1 kroku
sirka_B = 7
vyska_B = 8
x = 0
y = 0
while x+1:
    if x >sirka:
        x=0    
    vymaz()
    obdelnik("A",x+poc_x_A,poc_y_A,sirka_A,vyska_A)
    obdelnik("B",x+poc_x_B,poc_y_B,sirka_B,sirka_B)
    x+=1
    tisk()
    sleep(0.01)