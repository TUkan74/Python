

with open('odst.in','r',encoding = 'utf-8') as rf:
    with open('odst.out','w',encoding = 'utf-8') as wf:
        dlzka_riadku = int(rf.readline()) +1
        vsetko = rf.read().split()
        #vatiables
        buduca = ""
        veta= ""
        i=0
        dlzka = len(vsetko)
        
        vsetko.append(vsetko[dlzka-1]) 
        while i <dlzka:
            #variables
            #position of spaces
            medzera = [] 
         
            veta=vsetko[i]
            buduca=veta + " "+vsetko[i+1]
            i+=1
            index = 1
            medzera.append(len(veta))
            #vytvaranie riadku
            while len(buduca) < dlzka_riadku and i<dlzka:
                
                veta =veta+ " " + vsetko[i] 
                buduca = veta+ " " + vsetko[i+1] 
                #pozicie medzier
                medzera.append(len(veta))
                
                #var increase
                i+=1
                
                index+=1
            #adding spaces
            if i<dlzka-1 and index > 1: 
                while len(veta)< dlzka_riadku:
                    for j in range(len(medzera)-1):
                        
                        if len(veta) >= dlzka_riadku:
                            break
                        else: 
                            veta = veta[ : medzera[j]] + " " + veta[medzera[j] : ]
                            for k in range(j,len(medzera)):
                                medzera[k]+=1    
                        

                       
                      
            wf.write(veta)
            wf.write("\n")
        print("succes")        
            


    
