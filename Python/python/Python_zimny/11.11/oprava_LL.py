class Prvek:
    def __init__(self, h, d=None):
        self.hodnota = h
        self.dalsi = d


class LSS:
    def __init__(self):
        self.zac = None

    def PridejHodnotuNaZacatek(self, h):
       self.zac = Prvek(h,self.zac)
       
    def OtocSeznam(self):
        """Otočí seznam do opačného pořadí
        POZOR: nechceme vytvářet žádné nové prvky!!!
        Metodu PridejHodnotuNaZacatek() nemůžeme volat, protože
        tato metoda vytváři nové instance třídy Prvek!
        """
        nitr= self.zac.dalsi
        nnitr = None
        self.zac.dalsi = None

        while nitr:
            nnitr = nitr.dalsi
            nitr.dalsi = self.zac
            self.zac = nitr
            nitr = nnitr
            nnitr = None
        

    def VypustPrvek(self, p):
        """Vynechá ze seznamu prvek p (p je odkaz na prvek)
        p může byt None, nebo p nemusí být prvek v seznamu.
        """
        
        itr = self.zac
        prev= None
        
        while itr:
            if itr==p:
                if prev==None:
                    self.zac = itr.dalsi
                    return 
                else:
                    prev.dalsi = itr.dalsi
                    return 
            else: 
                prev = itr
                itr = itr.dalsi
                
        pass


    def VypustPrvkySHodnotou(self, h):
        """Vynechá ze seznamu všechny prvky s hodnotou h
        jsou-li tam nějaké.
        """
        itr = self.zac
        prev = None
        while itr:
            if itr.hodnota == h:
                if prev:
                    prev.dalsi = itr.dalsi
                    itr = itr.dalsi
                else: 
                    self.zac = itr.dalsi
                    itr = itr.dalsi
            else:
                prev = itr
                itr = itr.dalsi
                
        

       
    def VypustPrvkySHodnotouVetsiNez(self, h):
        """Vynechá ze seznamu všechny prvky s hodnotou ostře větší než h
        jsou-li tam nějaké.
        """
        itr = self.zac
        prev = None
        while itr:
            if itr.hodnota > h:
                if prev:
                    prev.dalsi = itr.dalsi
                    itr = itr.dalsi
                else:
                    self.zac = itr.dalsi
                    itr= itr.dalsi
            else:
                prev = itr
                itr = itr.dalsi
                
        pass

    def NajdiPrvekSHodnotou(self, h):
        """Hledá v seznamu první (od začátku) prvek s hodnotou h.
        Když tam je alespoň jeden prvek s hodnotou h, tak vrátí ten,
        který je nejblíže začátku seznamu.
        Když prvek s hodnotou h v seznamu není, tak funkce vrátí None.
        """
        itr = self.zac
        while itr:
            if itr.hodnota == h:
                return itr
            else:
                itr = itr.dalsi
        return None
                    
        pass

    def NajdiPrvekSHodnotouVetsiNez(self, h):
        """Hledá v seznamu nejmenší prvek (od začátku) s hodnotou větší než h.
        Vrátí prvek s nejmenší hodnotou, která je větší než h.
        Když je tam takových více, tak
        ten, který je nejblíže začátku seznamu.
        Když seznam neobsahuje žádné prvky s hodnotou větší h,
        tak funkce vrátí None.
        """
        itr = self.zac
        najmensi = self.zac
        while itr:
            if itr.hodnota > h :
                if najmensi:
                    if najmensi.hodnota > itr.hodnota:
                        najmensi = itr
                    else:
                        najmensi = itr
                itr = itr.dalsi
            else:
                itr = itr.dalsi
        return najmensi

    def Vypis(self):
        """vypise hodnoty ze sezanmu na jeden radek"""
        pom = self.zac
        while pom:
            print(pom.hodnota, end=' ')
            pom = pom.dalsi
        print('')       # konec radku
    
    

s = LSS()
pocet_prikazu = int(input())
for _ in range(pocet_prikazu):
    radek = input().split()
    prikaz = radek[0]
    parametry = radek[1:]
    if prikaz == 'OtocSeznam':
        s.OtocSeznam()
    elif prikaz == 'PridejHodnotuNaZacatek':
            s.PridejHodnotuNaZacatek(int(parametry[0]))
    elif prikaz == 'VypustPrvek':
        if parametry[0] == '=':
            p = s.NajdiPrvekSHodnotou(int(parametry[1]))
            s.VypustPrvek(p)
        elif parametry[0] == '>':
            p = s.NajdiPrvekSHodnotouVetsiNez(int(parametry[1]))
            s.VypustPrvek(p)
        else:
            print(f'Neznamy parametr v prikazu "{prikaz} {parametry[0]}"')
    elif prikaz == 'VypustPrvkySHodnotou':
        s.VypustPrvkySHodnotou(int(parametry[0]))
    elif prikaz == 'VypustPrvkySHodnotouVetsiNez':
        s.VypustPrvkySHodnotouVetsiNez(int(parametry[0]))
    elif prikaz == 'p':
        s.Insert_at_end(5)
    else:
        print(f'Neznamy prikaz "{prikaz}"',)
    s.Vypis()


