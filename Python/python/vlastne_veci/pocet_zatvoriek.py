string= "()()()()()()()((((()))))"
x=0
for i in range(len(string)):
    if string[i] == "(":
        x+=1
    elif string[i]: 
        x-=1
    if x<0:
        print("Zly pocet")
        break

if (x==0):
    print("Spravne")
else:
    print("Nespravne")                 