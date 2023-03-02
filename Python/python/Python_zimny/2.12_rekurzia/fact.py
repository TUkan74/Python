def fact(n):
    vysledok = 1
    if  n==1 or n ==0:
        return vysledok
    elif n<0:
        return 0
    else: 
        return n*fact(n-1)
print(fact(5))