class Vehicle:
    def __init__(self,seating_capacity):
        self.seating_capacity_bus = seating_capacity
          
    def seating_capacity(self):
        return "Bus setting capacites default is {}" .format(self.seating_capacity_bus)
        
   
class Bus(Vehicle):
    pass
        

vehicle_types = Bus(50)

print(vehicle_types.seating_capacity())

     



class Vehicles:
    def __init__(self,colour):
        self.color = colour
        self.cler = self.Colours()
        
    def show(self):
        print(self.cler.show())
        #return "every Vehicle should be {}" .format(self.color) 
        
    class Colours:
        def __init__(self):
            self.color = "white"
            
        def show(self):
            return "Vehicle should be with colour {}" .format(self.color)
            
      
c1 = Vehicles("white")



c1.show()

#constructor
 
class  constructor:
    def __init__(self):
        print("init c")
    def fet1(self):
        print("1")
       
class E(constructor):
    #def __init__(self):
        #pass
       # super().__init__()
       
    
    def feature(self):
        super().fet1()
        
c1 = E()

c1.feature()                    
    