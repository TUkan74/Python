class Prvek:
    def __init__(self,data,r = None,l = None,f = None):
        self.right = r
        self.left = l
        self.data = data
        self.father = f

class Strom:
    def __init__(self,data = None) :
        self.key