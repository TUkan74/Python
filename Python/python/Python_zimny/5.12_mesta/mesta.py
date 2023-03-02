N = int(input())
M = int(input())
Grupa_A = 0
Grupa_B = 0
Nejde = False
Rovnake = False

Cities_1 = set()
Cities_2 = set()

'''cesta = input().split()
A = int(cesta[0])
B = int(cesta[1])
Cities_1.add(A)
Cities_2.add(B)'''



for i in range(M):
    Grupa_A = 3
    Grupa_B = 4
    cesta_2 = input().split()
    A = int(cesta_2[0])
    B = int(cesta_2[1])

    if A in Cities_1:
        Grupa_A = 1

    if A in Cities_2 :
        Grupa_A = 2
    
    if B in Cities_1:
        Grupa_B = 1

    if B in Cities_2 :
        Grupa_B = 2
    
    
    if Grupa_A == Grupa_B:
        Nejde = True
        
    if A == B:
        Rovnake = True
        Nejde = False
   

    if Grupa_A == 3: 
        if Grupa_B == 1:
            Cities_2.add(A)
        if Grupa_B == 2:
            Cities_1.add(A)
        if Grupa_B == 4:
            Cities_1.add(A)
         
    
    if Grupa_B == 4:
        if Grupa_A == 1:
            Cities_2.add(B)
        if Grupa_A == 2:
            Cities_1.add(B)
        if Grupa_A == 3:
            Cities_2.add(B)
 
if Nejde :
    print("Nelze")
else:
    result_2 = ' '.join(str(item) for item in Cities_2)
    result_1 = ' '.join(str(item) for item in Cities_1)
    print(result_1)
    print(result_2)
     