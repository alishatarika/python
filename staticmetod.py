class math:
    @staticmethod
    def sum(a,b):
      print("your ans is ",a+b)
    def sub(t,a,b): #in normal method we have to pass self always but in static we donot need to pass 
        print("your ans is ",a-b)

a=math()
a.sum(3,5)
a.sub(6,7)

class Employee:
  company = "Apple" #class method
  def show(self):
    print(f"The name is {self.name} and company is {self.company}") #instance method

  @classmethod
  def changeCompany(cl, newCompany):
    cl.company = newCompany


e1 = Employee()
e2 = Employee()
e1.name = "Harry"
e2.name="alisha"
e1.show()
e1.changeCompany("Tesla")
e1.show()
e2.show()
print(Employee.company)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(self.name,self.age)
    @classmethod
    def from_string(cls, string):
        name, age = string.split(',')
        return cls(name, int(age))
    
person = Person.from_string("John Doe, 30")