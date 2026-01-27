# class Employee:
#     company = "ITC"
#     name = "Niranjan kumar"
    
#     # def __init__(self, name, salary):
#     #     self.name = name
#     #     self.salary = salary
    
#     def show(self):
#         print(f"The name of Employee is {self.name} and the company is {self.company}")
        
# class coder:
#     language = "python"
    
#     # def __init__(self, name, salary, language):
#     #     self.name = name
#     #     self.salary = salary
#     #     self.language = language

#     def printLanguage(self):
#         print(f"Out of all language here is your language {self.language}")

# class Programmer(Employee, coder):
#     company = "ITC Infotech"
        
#     def showLanguage(self):
#         print(f"The name of company is {self.company} and he is good with {self.language} language")
        

# a = Employee()
# b = Programmer()

# b.show()
# b.printLanguage()
# b.showLanguage()



# class Employee:
#     print("constructor of Employee")
#     a = 1

# class Programmer(Employee):
#     b = 2
    
# class Manager(Programmer):
#     c = 3
    
# o = Employee()
# print(o.a)

# o = Programmer()
# print(o.a, o.b)

# o = Manager()
# print(o.a, o.b, o.c)


# class Employee:
#     def __init__(self):
#         print("constructor of Employee")
#     a = 1

# class Programmer(Employee):
#     def __init__(self):
#         print("constructor of programmer")
#     b = 2
    
# class Manager(Programmer):
#     def __init__(self):
#         super().__init__()
#         print("constructor of manager")
#     c = 3
    
# o = Employee()
# print(o.a)

# o = Programmer()
# print(o.a, o.b)

# o = Manager()
# print(o.a, o.b, o.c)


# # Class Method
# class Employee:
#     a = 1
    
#     @classmethod
#     def show(cls):
#         print(f"The class attributes of a is {cls.a}")
        
# e = Employee()
# e.a = 45
# e.show()


# # Property Decorator
# class Employee:
#     a = 1
    
#     @classmethod
#     def show(cls):
#         print(f"The class attributes of a is {cls.a}")
        
#     @property
#     def name(self):
#         return self.ename
    
#     @name.setter
#     def name(self, value):
#         self.ename = value
        
# e = Employee()

# e.a = 45                 # instance variable
# e.ename = "niranjan"     # setter is called

# print(e.name)            # getter is called
# e.show()


a = "Niranjan yadav"
print(a.split(" "))
