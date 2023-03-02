def variace(k,n):
    def var(i):
      
      for j in range(1,n+1):
        v[i] = j
        if i< k-1:
            var(i+1)
        else:
            vysledok.append(v[:])
    v = [0] *k
    vysledok = []
    var(0)
    return vysledok
print(variace(2,5))
