def is_factorial(c):
    v=1
    i=1
    while v<c:
        i+=1
        v*=i
    if v==c:   
        return i

    else:
        return -1   
x=int(input())
print(is_factorial(x))            