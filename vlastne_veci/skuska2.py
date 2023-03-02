import numpy as np
'''A = [[2,0,0],
     [0,2,0]]
row_A = len(A)
col_A = len(A[0])
print(col_A)
print(row_A)     
'''
'''Dots = [n for n in range(8)]
Dots[0] =[[-2],[-2],[-2]]
Dots[1] =[[2],[-2],[-2]]
Dots[2] = [[2],[2],[-2]]
Dots[3] =[[-2],[2],[-2]]
Dots[4] =[[-2],[-2],[2]]
Dots[5] =[[2],[-2],[2]]
Dots[6] =[[2],[2],[2]]
Dots[7] =[[-2],[2],[2]]'''

Dots = [i for i in range(8)]
Dots[0] =[[-1],[-1],[-1]]
Dots[1] =[[1],[-1],[-1]]
Dots[2] =[[1],[1],[-1]]
Dots[3] =[[-1],[1],[-1]]
Dots[4] =[[-1],[-1],[1]]
Dots[5] =[[1],[-1],[1]]
Dots[6] =[[1],[1],[1]]
Dots[7] =[[-1],[1],[1]]

a = np.matrix([[-2, -2, -2],
               [2,  -2, -2]])
row_B = len(a[0])
col_B = len(a)

print(col_B)
print(row_B)