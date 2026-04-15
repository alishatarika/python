class student:
        name="Alisha"
        __rollno=345 #private variable
        def __prin(self):
            print(self.name,self.__rollno)
data=student()
print(data.name)
print(data._student__rollno)  #private access
data._student__prin()

#protected member
class Student:
    def __init__(self):
        self._name = "Harry"

    def _funName(self):      # protected method
        return "CodeWithHarry"

class Subject(Student):       #inherited class
    pass

obj = Student()
obj1 = Subject()

# calling by object of Student class
print(obj._name)      
print(obj._funName())     
# calling by object of Subject class
print(obj1._name)    
print(obj1._funName())