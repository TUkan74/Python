def palindrom(n):
    return n == n[::-1]
    
def rising(n):
    number = list(n)
    
    for i in range(len(number)-1):
        cur = int(number[i])
        next = int(number[i+1])
        if next % 10 != (cur+1) % 10:
            return False
    return True
    
def falling(n):
    
    number = list(n)
    
    for i in range(len(number)-1):
        print(number)
        print(i)
        cur = int(number[i])
        next = int(number[i+1]) 
        if cur % 10 != (next+1) % 10:
            return False
        if next == 9 and cur == 0:
            return False   
    return True
    
def zeros(n):
    return n[1:] == (len(n) - 1) * '0'

def order(i):
    if i == 0:
        return 2
    return 1
    

def same(n):
    return n == len(n) * n[0]

def is_awesome_phrase(string, phrases):
    number = int(string)
    for phrase in phrases:
        if number == int(phrase):
            return True
    return False

def is_interesting(number, awesome_phrases):
    
    
    if number < 98:
        return 0
    
    
        
    for i in range(3):
        n = str(number+i)
        poradie = order(i)
        
        if int(n)>99:
            if palindrom(n):
                return "palindron"

            elif rising(n):
                if int(n):
                    return "rising"

            elif falling(n):
                if int(n):
                    return "falling"

            elif zeros(n):
                return "zeros"

            elif same(n):
                return "same"

            elif is_awesome_phrase(n,awesome_phrases):
                return "ap"
        
         
    
    return 0

print(is_interesting(109,[1337, 256]))