def res(n,array):
    dlzka = len(array)
    vysledok = str(n)+'='+ str(array[0])
    for i in range(1,dlzka):
        vysledok = vysledok +"*"  + str(array[i])
    return vysledok

def fact(num ):
    vysledok= []
    i=2
    n = num
    while i*i <=num:
        if num %i !=0:
            i+=1
        else:
            num //=i
            vysledok.append(i)
    if num>1:
        vysledok.append(num)
    return res(n,vysledok)

print(fact(28))