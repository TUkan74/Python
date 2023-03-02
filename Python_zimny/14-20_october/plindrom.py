def ispalindrom(s):
    return s==s[::-1]

x='1'

while x!="0": 
    x=(input())

    if (ispalindrom(x) and x!=" " and x!="" and x!="0") :
        print(x,end=" ")    
              





