# kresleni na platno
#
# levy dolni roh platna ma souradnice (0,0), pravy horni roh ma souradnice (sirka-1,vyska-1)
# prvni souradnice je horizontalni, druha vertikalni



class Platno:
    def __init__(self, sirka=60, vyska=12, prazdny_znak='.'):
        self.sirka = sirka
        self.vyska = vyska
        self.platno = []
        self.pozadi = prazdny_znak
        for i in range(self.vyska):
            self.platno.append([prazdny_znak] * self.sirka)

    def vymaz(self, prazdny_znak=None):
        if prazdny_znak is None:
            prazdny_znak = self.pozadi
        for i in range(self.vyska):
            for j in range(self.sirka):
                self.platno[i][j] = prazdny_znak

    def tisk(self):
        print("=" * self.sirka)
        for i in range(self.vyska - 1, -1, -1):
            for j in range(self.sirka):
                print(self.platno[i][j], end='')
            print()
        print("=" * self.sirka)

    def vloz_bod(self, znak, x, y):
        if 0 <= x < self.sirka and 0 <= y < self.vyska:
            self.platno[y][x] = znak


class Obdelnik:
    def __init__(self, znak, sirka, vyska):
        # obdelnik sirky sirka a vysky vyska skladajici se ze znaku znak
        self.znak = znak
        self.sirka = sirka
        self.vyska = vyska

    def nakresli(self, platno, posun_x=0, posun_y=0):
        for j in range(posun_y, posun_y + self.vyska):
            for i in range(posun_x, posun_x + self.sirka):
                platno.vloz_bod(self.znak, i, j)


class Utvar:
    def __init__(self, prvky=None):
        # Utvar se sklada se z prvku, ktere maji svoje posunuti
        # relativni k Utvaru. Kazdy prvek je trojice (objekt, posun_x, posun_y)
        # prvky utvaru jsou ulozene v seznamu prvky
        pass

    def pridej_prvek(self, prvek, posun_x=0, posun_y=0):
        pass

    def nakresli(self, platno, pos_x=0, pos_y=0):
        # nakresli utvar skladajici se z jednotlivych prvku
        # utvar je posunuty v x-ove souradnici o pos_x
        # a v y-ove souradnici o pos_y
        pass

platno = Platno()
print('Prazdne platno')
platno.tisk()

obrazek = Utvar()
o = Obdelnik('X', 6, 3)
obrazek.pridej_prvek(o)
print('Platno s obdelnikem 6x3 v levem dolnim rohu')
obrazek.nakresli(platno)
platno.tisk()

print('Platno se dvema obdelnikama')
platno.vymaz()
obrazek.nakresli(platno)
# pridame kopii obdelniku 6x3 posutou o 10 vodorovne a o 3 svisle
obrazek.pridej_prvek(o, 10, 3)
obrazek.nakresli(platno)
platno.tisk()



# sestavte auto skladajici se nekolika obdelniku
#............................................................
#............................................................
#............................................................
#.............BBBBBBBBBBBBBB.................................
#.............B.....BB.....B.................................
#.............B.....BB.....B.................................
#.......AAAAAAAAAAAAAAAAAAAAAAA..............................
#.....AAAAAAAAAAAAAAAAAAAAAAAAA..............................
#.........OOOOO.........OOOOO................................
#..........OOO...........OOO.................................
#............................................................
#............................................................
#============================================================
platno.vymaz()

kolo = Utvar()
kolo.pridej_prvek(Obdelnik('O', 3, 1), 1, 0)
kolo.pridej_prvek(Obdelnik('O', 5, 1), 0, 1)
kola = Utvar()
kola.pridej_prvek(kolo, 9, 2)
kola.pridej_prvek(kolo, 25, 2)

kola.nakresli(platno)
platno.tisk()

# dokoncete kresleni auta:
#   karoserie jsou dva obdelniky
#   okna jsou dve mensi okna
#   mensi okno je obdelnik, ktery ma uvnitr prazny obdelnik
#

# udelejte animaci s alespon dvema auty

# rozsirte tridu Utvar o zrcadlove otoceni


