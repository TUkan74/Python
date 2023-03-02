class VrcholBinStromu:
    def __init__(self,x= None,l = None,r = None) :
        self.data = x
        self.left = l
        self.right = r
    
    def vyhladaj(self,vrchol,key):
        if vrchol is None or key == vrchol.data:
            return vrchol
        
        if key < vrchol.data:
            return vyhladaj(vrchol.left,key)
        else:
            return vyhladaj(vrchol.right,key)
    
    def uloz(self,koren,key):
        if koren == None:
            koren == VrcholBinStromu(key)
        
        elif key < koren.data:
            koren.left = uloz(koren.left,key)

        elif key> koren.data:
            koren.right = uloz(koren.right,key) 

        return koren