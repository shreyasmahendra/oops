class A:
    def __init__(self):
        print("inheritance")
    
    def feture1(self):
        print("inheritance1")
    def feture2(self):
        print("inheritance2")
        
class B(A):
    def feture3(self):
        print("inheritance3")
        
a1 = A()
a1.feture1()
b1 = B()
b1.feture1()


class C:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
        
    def __add__(self):
        r1 = self.m1 + self.m2
        return r1 
    def __sub__(self):
        r1 =  self.m1 - self.m2
        return r1
    def __mul__(self):
        r1 = self.m1 * self.m2
        return r1
    def __div__(self):
        r1 = self.m1 / self.m2
        return r1

r1 = C(10,20)
r2 =C(10,20)

print(r1.__add__())
print(r1.__sub__())
print(r1.__mul__())
print(r1.__div__())

class XY:
    #def __init__(self,a1,b1,c1):
        #self.a = a1
        #self.b = b1
        #self.c = c1 
    def get(self):
        return self.a 
       
        
    def set(self,value1):
        self.a = value1
       
        
x1 = XY()
x1.set("a")
print(x1.get())   


class Vehicle:
    def __init__(self):
        self.max_speed = 40
        self.mileage = 30
        
a1 = Vehicle()        
