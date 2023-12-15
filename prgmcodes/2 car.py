class car:
    def __init__(self,color,price,kilometer):
        self.price=price
        self.color=color
        self.kilometer=kilometer
    def __gt__(self,other):
        if(self.price>other.price):
            return True
        else:
            return False
    def __add__(self,other):
        return self.kilometer+other.kilometer
car1=car("black",100,45)
car2=car("red",50989000,10)
sum=car1.kilometer+car2.kilometer
print("kilometer",sum)
if(car1.price>car2.price):
    print("car1 is more expensive than car2")
else:
    print("car2 is more expensive than car1")
    


        
            
            
