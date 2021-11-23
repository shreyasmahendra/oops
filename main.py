class computer:

    def __init__(self,a,b):
        self.a = a
        self.b = b
        
        
    def config(self):
        print("shreyas", self.a, self.b)
        
comp1 = computer('a','b')

#computer.config(comp1)

comp1.config()

comp2 = computer('i5',16)
comp2.config()       

#########################################

class something:
    def __init__(self):
        self.name ="shreyas"
        self.age = 23
    
    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False
            
c1 = something()
c2 = something()
c2.age = 33

if c1.compare(c2):
    print("same")
else:
    print("not same")


print(c2.name)
'''
3 types of methods
class methods 
instances methods 
static methods
'''
###################################################

class car:
    #class varables
    wheels = 4
    
    def __init__(self):
        #instance varables
        self.mill =10
        self.com = "bmw"
        
c1 = car()

#c1 is the object name we can use it to cal instant varables
c1.mill = 8
#car is the class name so for class varable to access we can use car or object as c1
car.wheels = 6

print(c1.com,c1.mill,c1.wheels,car.wheels)        

#########################################

class stu:
    school ="ijrs"
    
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 =m2
        self.m3 = m3
    
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
#decoraters used to access class varables so we dont want to pass cls as a parameter so        
    @classmethod    
    def info(cls):
        return cls.school
    
    @staticmethod
    def getSchool():
        print("this is a static method we can use for our use just to know like factorial like that ")
    
    
    
s1 = stu(34,33,33)
print(s1.avg())   
print(stu.info())#we must pass a parameter inside as cls but we r using decoratores so we need not  
stu.getSchool()#we need not use class or object to this static methods        
##############################################

'''
we can define insede class and the inside class can be obtained by outside class 
'''

class students: #outer class
    def __init__(self,name,rollno):
        self.name = name 
        self.rollno = rollno
        self.lap = self.Laptop() 
        
    def show(self):
        print(self.name,self.rollno)
        self.lap.show()
        
    class Laptop: #inner class
        def __init__(self):
            self.brand ='hp'
            self.cpu ='i5'
            self.ram = 8
        def show(self):
            print(self.brand,self.cpu,self.ram)

s1 = students('shreyas',2)
s1.show()            

'''
inheritance = 
'''

class A: #parentclass /super class
    def feture1(self):
        print("inheritence  1")
        
    def feture2(self):
        print("going on 2")
        
class B(A): #child class /sub class
    def feture3(self):
        print("hi 3 ")
        
    def feture4(self):
        print("welcome 4")
        
class C(B):#multiple inheritance
    def feture5(self):
        print("fjkfk 5")    
       
a1 = A()

a1.feture1()
a1.feture2()

b1 = B()       
c1 = C()
c1.feture3() 
c1.feture4()
b1.feture1()

'''
 constructor,mro = method resolution order it calls from left to right
 the object first calls the innit method and then if init is in b then it first calls b init and then a 
 
'''
 
class  C:
    def __init__(self):
        print("init c")
    def fet1(self):
        print("1")
        
class D:
    def __init__(self):
        print("init d")
    def fet2(self):
        print("2")

class E(C,D):
    def __init__(self):
        super().__init__()
        print("e")
    
    def feat(self):
        super().fet1()
        
c1 = E()

c1.feat()        
        
'''
polymorphism when we use it loose coupling ,interface,dependency injection
duck typing
operator overloading
method overloading
method overriding
'''
#this is duck typing  we just use execute method inside the class and we call it like ide = classname
class Myeditor:
    def execute(self):
        print("compiling")
        print("running")
    
class Lap:
    def code(self,ide):
        ide.execute()

ide = Myeditor()

l1 = Lap()
l1.code(ide) 
#########################################

class S:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
        
    def __add__(self,other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = S(m1,m2)
        return s3
    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False
    def __str__(self):
        return '{} {}'.format(self.m1,self.m2)
    
    
s1 =S(58,69)
s2 = S(90,10)

s3 = s1 + s2
print(s3.m1)
print(s3.m2)        

if s1 > s2:
    print("s1 is greater")
else:
    print("s2 wins")
    
print(s1)
print(s2.__str__)    
# operator overloading

      
    
        