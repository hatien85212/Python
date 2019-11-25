class MyClass:
  x = 5
  __y =10 #data hiding: to access the value, p1._MyClass__y, name manling
  __z__=15
  _t = 20 #private variable
  
p1 = MyClass() #All classes have a function called __init__(), is called automatically every time the class is being used to create a new object.
print(p1.x)
#print(p1.y) #to hide data of "y" on "MyClass", this varible need to add double underscore at beginning
print (p1._MyClass__y)
print (p1.__z__)
print (id(p1))
print (p1._t)
#dir(p1) #return the strings: varialbe, methods
  
class Person:
  #class methods: the first one is self -- reference to the current instance of class, don't need include when calling
  #purpose of the __init__() method is to initialize the class. It is usually responsible for populating the instance variables.
  def __init__(self, name, age, sex="male"): #constructor
    self.name = name
    self.age = age
    self.sex = sex
	
  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("John", 36)
p1.sex="female" #instance variable: female
print (p1.sex)
p2 = Person("Tien", 34)
print (p2.sex)
p1.myfunc()
p2.myfunc()

"""You can add, remove, or modify attributes of classes and objects at any time 
emp1.age = 7  # Add an 'age' attribute.
emp1.age = 8  # Modify 'age' attribute.
del emp1.age  # Delete 'age' attribute.
#Instead of using the normal statements to access attributes, you can use the following functions
hasattr(emp1, 'age')    # Returns true if 'age' attribute exists
setattr(emp1, 'age', 8) # Set attribute 'age' at 8
getattr(emp1, 'age')    # Returns value of 'age' attribute
delattr(empl, 'age')    # Delete attribute 'age'
"""

"""Built-In Class Attributes
#__dict__ Dictionary containing the class's namespace.
#__doc__ Class documentation string or none, if undefined.
#__name__ Class name.
#__module__ Module name in which the class is defined. This attribute is "__main__" in interactive mode.
__bases__ A possibly empty tuple containing the base classes, in the order of their occurrence in the base class list.
"""

#Class Inheritance
class Parent:        # define parent class
   parentAttr = 100
   def __init__(self):
      print "Calling parent constructor"

   def parentMethod(self):
      print 'Calling parent method'

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print "Parent attribute :", Parent.parentAttr
   def _method(self): #private method, ignored from import module
		print "Parent private method"

class Child(Parent): # define child class, class C(A, B):   # subclass of A and B
  # def __init__(self): #override parent construtor 
   #   print "Calling child constructor"

   def childMethod(self):
      print 'Calling child method'
   def parentMethod(self): #overriding parent method
      print 'Override parent method'
	  
"""Base Overloading Methods: https://www.tutorialspoint.com/python/python_classes_objects.htm
__init__ ( self [,args...] )
__del__( self )
__repr__( self )
__str__( self )
__cmp__ ( self, x )
"""

c = Child()          # instance of child. Calling child constructor if uncomment the constructor in child class
c.childMethod()      # child calls its method, Calling child method
c.parentMethod()     # calls parent's method, Override parent method
c.setAttr(200)       # again call parent's method
c.getAttr()          # again call parent's method, Parent attribute : 200
c.parentMethod()	 # calls parent's method, Override parent method
c._method()
dir(c)

# Overloading Operators
class Vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b

   def __str__(self):
      return 'Vector (%d, %d)' % (self.a, self.b)
   
   def __add__(self,other):
      return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2,10)
v2 = Vector(5,-2)
print v1 + v2

# Multiple inheritance
class Coral:
    def community(self):
        print("Coral lives in a community.")

class Anemone:
    def protect_clownfish(self):
        print("The anemone is protecting the clownfish.")

class CoralReef(Coral, Anemone):
    pass
	
great_barrier = CoralReef()
great_barrier.community()
great_barrier.protect_clownfish()

class Fish:
    def __init__(self, first_name, last_name="Fish",
               skeleton="bone", eyelids=False):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids

    def swim(self):
        print("The fish is swimming.")

    def swim_backwards(self):
        print("The fish can swim backwards.")
#Fish inheritance		
class Trout(Fish):
    #pass #undefine anything, use the same parent class
	def __init__(self, water = "freshwater"): #use all the same all, excluding add more att water
        #self .water = water
        #super().__init__(self)
        pass

class Clownfish(Fish):

    def live_with_anemone(self):
        print("The clownfish is coexisting with sea anemone.")
class Shark(Fish): #overrid swim_backwards method, override eyelids
    def __init__(self, first_name, last_name="Shark",
                 skeleton="cartilage", eyelids=True):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids

    def swim_backwards(self):
        print("The shark cannot swim backwards, but can sink backwards.")
# Trout	
terry = Trout("Terry")
print(terry.first_name + " " + terry.last_name)
print(terry.skeleton)
print(terry.eyelids)
terry.swim()
terry.swim_backwards()
# Clownfish: have live_with_anemone
casey = Clownfish("Casey")
print(casey.first_name + " " + casey.last_name)
casey.swim()
casey.live_with_anemone()
# Shark
sammy = Shark("Sammy")
print("Shark: " + sammy.first_name + " " + sammy.last_name)
sammy.swim()
sammy.swim_backwards()
print(sammy.eyelids)
print(sammy.skeleton)