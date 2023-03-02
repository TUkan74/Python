def je_tam(x,y):
    
    dlzka= len(x)-1
    d=dlzka
    rovnake=0
    
    for i in range(len(y)-1,0,-1):
        
        
        
        if (x[dlzka] == y[i]):
            rovnake+=1
            dlzka-=1
        
        else:
            rovnake=0
            dlzka=len(x)-1
        
        if rovnake==3:
            vysledok= set()
            vysledok.add((i,i+d))
            return vysledok  

hladam=[1,1,1]
kde=[1,2,1,2,3,1,1,1]
index=je_tam(hladam,kde)
#print("Nachadza sa na pozicii: ",index,"az:",index+len(hladam)-1 )
print("Nachadza sa na pozicii: ",je_tam(hladam,kde) )                
            