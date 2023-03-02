a=1
vysledok=0

while a!=0:
    x=input().split()
    i=0
    while a!=0 and i<len(x):
        a=int(x[i]);
        vysledok+= a
        i+=1
print(vysledok)        


    

    
    

    