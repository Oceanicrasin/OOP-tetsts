class dog:
    def __init__(self, name):
        self.name=name
        self.tricks=[] # creates a new empty list for each dog
        
    def add_trick(self,trick):
        self.tricks.append(trick)
class Warehouse:
    purpose = "storage"
    region = "west"
    
w1 = Warehouse()
print(w1.purpose, w1.region)
w2 = Warehouse()
w2.region = "east"
print(w2.purpose, w2.region)        
    
Bentley=dog("Bentley")
Bentley.add_trick("playing dead")
print(Bentley.tricks)
