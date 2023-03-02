class Stack:
    def __init__(self) :
       self.pole = []
    
    def __len__(self):
        return len(self.pole)

    def empty(self):
        return len(self.pole) == 0

    def push(self,x):
        self.pole.insert(0,x)
    
    def pop(self):
        return self.pole.pop(0)

class Queue:
    def __init__(self):
        self.pole = []
    
    def __len__(self):
        return len(self.pole)

    def empty(self):
        return len(self.pole) == 0

    def enqueue(self,x):
        self.pole.append(x)

    def dequeue(self):
        self.pole.pop(0)

class Cycle_Q:
    def __init__(self,kapacita):
        self.zacatek,self.konec = 0,0
        self.pole = [None] * kapacita
        self.kapacita = kapacita

    def empty(self):
        return self.zacatek == self.konec
    
    def enqueue(self,x):
        novy = self.konec + 1 % self.kapacita
        self.pole[self.konec] = x
        self.konec = novy
    
    def dequeue(self):
        x = self.pole.pop(self.zacatek)
        self.zacatek = (self.zacatek + 1) 
        return x


pridaj = input().split()
zasobnik = Stack()
rada = Queue()
cykel = Cycle_Q(len(pridaj))
for i in pridaj:
    zasobnik.push(i)
    rada.enqueue(i)
    cykel.enqueue(i)
    
    
print(cykel.dequeue())
print(cykel.dequeue())
print(cykel.dequeue()) 
print(rada.pole)
print(zasobnik.pole)
print(cykel.pole)    

