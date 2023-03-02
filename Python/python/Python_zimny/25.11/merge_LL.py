class Prvek:

    def __init__(self, h, popis):
        self.hodnota = h
        self.popis = popis
        self.dalsi = None     #  tady si prvek pamatuje naslednika

class SetridenySeznam:
 
    def __init__(self):
        # seznam ma odkaz na prvni prvek seznamu, ktery ma minimalni hodnotu v seznamu
        self.zac = None

 
    def vloz(self, h, popis):
        """Vlozi do seznamu novy prvek s hodnotou h.
        Kdyz tam uz prvek s hodnotou h je v seznamu, tak prida dalsi kopii.
        """
        itr = Prvek(h,popis)

        if self.zac == None:
            self.zac = itr
        
        elif self.zac.hodnota >= itr.hodnota:
            itr.dalsi = self.zac 
            self.zac = itr
        else:
            temp = self.zac
            while temp.dalsi and itr.hodnota > temp.dalsi.hodnota:
                temp = temp.dalsi
            itr.dalsi = temp.dalsi
            temp.dalsi = itr
            
                
        # TADY PRIJDE VAS KOD
        
        
 

    def vypis(self):
        """vypise prvky seznamu na jeden radek"""
        pom = self.zac
        while pom:
            print('(', str(pom.hodnota), ',', pom.popis, ')',sep='', end=' ')
            pom = pom.dalsi
        print('')       # konec radku

def slejDestruktivne(s1, s2):
    '''Slej dva setridene seznamy s1 a s2 do jednoho setrideneho seznamu novy.
    Nebudou se vytvaret zadne nove prvky ani jine datove struktury. Seznamy
    s1 a s2 budou touto operaci zniceny a na konci zustanou prazdne!
    '''
    if not s1: novy=s2
    if not s2: novy=s1
    
    novy = SetridenySeznam()
    dummy = Prvek(0,0)
    itr1 = seznam1.zac
    itr2 = seznam2.zac
    tail = dummy
    
    
    
    
    
    while itr1 and itr2:
        if itr1.hodnota < itr2.hodnota:
            tail.dalsi = itr1
            seznam1.zac = itr1.dalsi
            itr1 = itr1.dalsi
        else:
            tail.dalsi = itr2
            seznam2.zac = itr2.dalsi 
            itr2 = itr2.dalsi
        tail = tail.dalsi
    dummy = dummy.dalsi
    novy.zac = dummy
    
    
    if  itr1: 
        
        tail.dalsi = itr1
    if  itr2: 
        
        tail.dalsi = itr2 
        
    
   
    
    

    # nasledujici radky musi zustat na konci funkce, aby se zarucilo, ze
    # seznamy s1 a s2 zustanou prazdne.
    s1.zac = None   
    s2.zac = None
    return novy 

delka1, delka2 = [int(i) for i in input().split()]

seznam1 = SetridenySeznam()
for _ in range(delka1):
    line = input().split()
    seznam1.vloz(int(line[0]), line[1])
seznam1.vypis()

seznam2 = SetridenySeznam()
for _ in range(delka2):
    line = input().split()
    seznam2.vloz(int(line[0]), line[1])
seznam2.vypis()

novy = slejDestruktivne(seznam1, seznam2)

novy.vypis()
                
