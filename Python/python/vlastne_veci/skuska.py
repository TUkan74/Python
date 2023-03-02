

wh= set()
wh.add("123456789")
stvorec=set()
stvorec.add("987654321")
zoznam = [0]*9
riadok=int((2/3) * 3)
  
if (1,3) in wh:
    print("Je tam")
    print(int(2/3))
    
'''x=[1,2,3]
print(len(x)) 
for i in range(len(x)-1,0,-1):
    print(i)''' 
for i in range(9):
    for j in range(0,6):
        if j==3:
            print("tu to konci",j)
            je=0
            break
        if j!=3:
            print(j)
    if je==0:
        break              