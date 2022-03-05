class CollectionService:
    def __init__(self):
        self.tab=[]
    
    def Add(self,c):
        self.tab.append(c)

    def Delete(self,c):
        self.tab.remove(c)


    def Show(self):
        for x in self.tab:
            print(x.marka, x.rok, x.przebieg)