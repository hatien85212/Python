class Employee: #Class: A user-defined prototype
	'Common base class for all employees'
	
	empCount=0 #Class variable:  is shared by all instances of a class, not used as frequently as instance variables are; accessed as Employee.empCount from in/out side of class
	raise_amt = 1.04
	#class methods: the first one is self -- reference to the current instance of class, don't need include when calling
	def __init__(self, name, salary): #constructor or initialization method
		self.name=name
		self.salary=salary
		Employee.empCount+=1
		
	def displayCount(self): 
		print ("Total Employee %d" % Employee.empCount)
	def displayEmployee(self):
		print ("Name : ", self.name,  ", Salary: ", self.salary)
	def fullName(self):
		return '{} {}'.format(self.name, "Name")
	def updateRaiseAmount(self, amount):
		Employee.raise_amt = amount
	
	@classmethod 
	def c_setRaiseAmount(cls, amount): #@classmethod decorator, call by using the class name instead of the object
	#A decorator is a function that receives another function as argument. A nested function
		cls.raise_amt = amount

"This would create first object of Employee class"
emp1 = Employee("Zara", 2000) #Create a new instance object of this class
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee() #Name :  Zara ,Salary:  2000
emp2.displayEmployee() #Name :  Manni ,Salary:  5000
print ("Total Employee %d" % Employee.empCount) #Total Employee 2

emp1.updateRaiseAmount(1.05)
Employee.c_setRaiseAmount(1.06)
print (Employee.raise_amt)

print ("Employee.__doc__:", Employee.__doc__) # 'Employee.__doc__:', 'Common base class for all employees'
print ("Employee.__name__:", Employee.__name__) #('Employee.__name__:', 'Employee')
print ("Employee.__module__:", Employee.__module__) #('Employee.__module__:', '__main__')
print ("Employee.__bases__:", Employee.__bases__)
print ("Employee.__dict__:", Employee.__dict__)

"""
"""

print (id(emp1), id(emp2))

emp1.age = 7  # Add an 'age' attribute.
emp1.age = 8  # Modify 'age' attribute.
print (emp1.age)

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
