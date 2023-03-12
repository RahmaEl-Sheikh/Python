def swapKeyValue (**kwargs):
        newDict={}
        for k,v in kwargs.items():     
            newDict[v]=k
        return newDict

print(swapKeyValue(Name="Rahma",Jop="engineer"))