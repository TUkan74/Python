def sum(n):
    if n <= 0:
        return 0
    else: 
        return n+sum(n-1)

#print(sum(4))

def grid_path(m,n):
    if m ==1 or n ==1:
        return 1
    else: 
        return grid_path(m,n-1) + grid_path(m-1,n) 
    
#print(grid_path(3,3))

def count_partition(n,m):
    if n ==0 :
        return 1
    elif m ==0 or n <0:
        return 0 
    else:
        return count_partition(n-m,m) + count_partition(n,m-1)  

print(count_partition(9,5))