import random

def big_array(arr):
    for i in range(len(arr)):
        arr[i]=i
    return arr    


def binary_search(arr,cislo):
    max=len(arr)-1
    mid=0
    min=0
    while min <= max:
        
        mid = (max + min) //2

        if arr[mid] < cislo:
            min = mid+1
        
        elif arr[mid] > cislo:
            max = mid - 1
        
        else:
            return mid        
    
#arr = [1,2,3,4,5,6,7,8,9,100,231,2110,10000,99999]
arr= [0] * 1000
arr= big_array(arr)
cislo=int(input("najdi cislo: "))
vysledok=binary_search(arr,cislo)            


print("cislo",cislo,"sa nachadza na mieste s indexom: ",vysledok)