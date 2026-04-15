# class data:
#  name=" "
#  occupation=" "
#  roll_no=98
#  def info(self):
#      print(f"{self.name} is a {self.occupation}")
#      return self.roll_no
 
     
# a=data()
# a.name=8
# a.occupation="software engineer"
# print(a.info())
# a.info()

# class cons:
#     def __init__(self,name1,roll_no1):
#       self.name=name1
#       self.roll_name=roll_no1
#       print(f"{self.name} is a {roll_no1}")
# a=cons("alisha",567)
# print(a.name)
# print(a.roll_name)

# '''
# def greet(fn):
#     def mf():
#         print("hello")
#         print("namaste")
#         fn()  
#         print("done")
#     return mf

# @greet
# def add():
#     a = 9
#     b = 8
#     print(a + b)

# add()



# class MyClass:
#     def __init__(self, value):
#         self._value = value
#     @property
#     def value(self):
#         return self._value
#     @value.setter
#     def value(self, new_value):
#         self._value = new_value
        
# obj = MyClass(10)
# obj.value = 20


# #super keyword
# class ParentClass:
#     def parent_method(self):
#         print("This is the parent method.")
# class ChildClass(ParentClass):
#     def parent_method(self):
#         print("This is the child method.")
#         super().parent_method()
# child_object = ChildClass()
# child_object.parent_method()

# #polymorphism
# class Bird:
#     def intro(self):
# 	    print("There are many types of birds.")
	
#     def flight(self):
# 	    print("Most of the birds can fly but some cannot.")

# class sparrow(Bird):
#     def flight(self):
# 	    print("Sparrows can fly.")
	
# class ostrich(Bird):
#     def flight(self):
# 	    print("Ostriches cannot fly.")
	
# obj_bird = Bird()
# obj_spr = sparrow()
# obj_ost = ostrich()

# obj_bird.intro()
# obj_bird.flight()

# obj_spr.intro()
# obj_spr.flight()

# obj_ost.intro()
# obj_ost.flight()
# '''
def my_gen():
    nums = [1, 2, 3]
    it = iter(nums)
    yield it
    print(it)
    yield it
    print(it)
    yield it
    print(it)
    yield it
    print(it)

