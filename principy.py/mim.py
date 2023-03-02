import random
minimum = 1
maximum = 2
kolik = 30

def tahni_hracem(kolik):
    print("na hromadce je ",kolik,"prvku")
    odebrat = 0
    while (odebrat<minimum or odebrat>maximum):
        print("racte tahnout")
        odebrat = int(input())
    return odebrat
while kolik>0:
    odeber = tahni_hracem(kolik)
    kolik-=odeber
    if kolik == 0:
        print("vyhralhrac")
    else:
        #odeber = tahni_Strojem(kolik)
        if kolik==0:
            print("prehral si")

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Nedokoncene !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!