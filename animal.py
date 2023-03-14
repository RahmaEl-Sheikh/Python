#Q9&10
class Animal:
    name=''
    def __init__(self,name):
        self.name=name
        print(self.name)
class Pet:
    owner=''
    def __init__(self,owner):
        self.owner=owner
        print(self.owner)
class Dog(Animal,Pet):
    breed=''
    def __init__(self,breed,name,owner):
        self.breed=breed
        print(self.breed)
        Animal.__init__(self,name)
        Pet.__init__(self,owner)
        
d1=Dog('jockey','roma','hasky')