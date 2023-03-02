def mocninal(x,n):
    v=1
    while n > 0:
        if n % 2 == 1:
            v *= x
        x *= x
        n //= 2
    return v
#casolva slozitosy theta (log N) - pocet opakovani while-cyklu     