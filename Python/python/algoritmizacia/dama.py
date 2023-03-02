def n_dam(n):

    def generuj_n_dam(radek):
        if radek == n: # riesenie uplne
            vysledok.append(list(sachovnica))
        else:
            for sloupec in range(n):
                if all(
                        abs(sachovnica[i]-sloupec) not in (0,radek-i)
                        for i in range(radek)):
                    sachovnica[radek] = sloupec
                    generuj_n_dam(radek+1)
    
    vysledok,sachovnica = [], [0]*n
    generuj_n_dam(0)
    return vysledok

def vypis(vysledok):
    if not vysledok : print("ziadne riesenie")
    else:
        n = len(vysledok[0])
        for sachovnica in vysledok:
            for i in range(n):
                for j in range(n):
                    if sachovnica[i]==j:
                        print("D",end= " ")
vypis(n_dam(4))