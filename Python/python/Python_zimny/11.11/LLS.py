class Prvek:
    def __init__(self, h, d=None):
        self.hodnota = h
        self.dalsi = d


class LSS:
    def __init__(self):
        self.zac = None

    def PridejHodnotuNaZacatek(self, h):
        self.zac = Prvek(h, self.zac)

    def OtocSeznam(self):

        pre = None
        x = self.zac
        nextx = x.dalsi

        while x:
            x.dalsi = pre
            pre = x
            x = nextx
            if nextx:
                nextx = nextx.dalsi
        self.zac = pre

    def VypustPrvek(self, p):

        if not p:
            return
        prev = None
        x = self.zac

        if x:
            if x.hodnota == p:
                self.zac = x.dalsi
                x = None
                return
        while x:
            if x.hodnota == p:
                break
            prev = x
            x = x.dalsi

        if x == None:
            return

        prev.dalsi = x.dalsi
        x = None
        pass

    def VypustPrvkySHodnotou(self, h):

        x = self.zac
        prev = None

        if not h:
            return None

        while x != None and x.hodnota == h:
            self.zac = x.dalsi
            x = self.zac

        while x != None:

            while x != None and x.hodnota != h:
                prev = x
                x = x.dalsi

            if x == None:
                return self.zac

            prev.dalsi = x.dalsi

            x = prev.dalsi
        return self.zac

    def VypustPrvkySHodnotouVetsiNez(self, h):

        if not h:
            return None

        prev = None
        x = self.zac

        while x:

            if x.hodnota > h:

                if x:
                    prev.dalsi = x.dalsi
                    x = x.dalsi
                else:
                    self.zac = x.dalsi
                    x = x.dalsi
            else:
                prev = x
                x = x.dalsi

        pass

    def NajdiPrvekSHodnotou(self, h):

        if not h:
            return None

        x = self.zac

        while x:
            if x.hodnota == x:
                return x

            x = x.dalsi

        return False

        pass

    def NajdiPrvekSHodnotouVetsiNez(self, h):

        if not h:
            return None

        x = self.zac
        min = self.zac

        while x:
            if x.hodnota > h and min.hodnota > x.hodnota:
                min = x
            x = x.dalsi

        return min
        pass

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
    else:
        print(f'Neznamy prikaz "{prikaz}"',)
    s.Vypis()