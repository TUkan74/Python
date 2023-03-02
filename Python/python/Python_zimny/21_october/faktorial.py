def faktorial(c):
    vysledok=1
    for i in range(1,c+1):
        vysledok*=i
    return vysledok
x=0
while x!=-1:
    x=int(input())
    print(faktorial(x))    