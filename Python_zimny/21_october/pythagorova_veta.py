

intcisla= [int(i) for i in input().split()]

vysledok=0
for m in range(len(intcisla)):
    c= intcisla[m]
    vysledok=0
    for b in range(2,c+1):
    
        for a in range(1,b+1):
        
            if (a*a + b*b) == c*c:
                vysledok+=1
        
            else:
                a+=1
    print(c,vysledok)            
                
    












