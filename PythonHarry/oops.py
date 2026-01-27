# class Employee:
#     name  = "niranjan"
#     language = "english"  # This is class attributes
#     salary = 120000000
    

# niranjan = Employee()    # This is object attributes
# niranjan.language = "python"
# print(niranjan.name, niranjan.language) 

# rohan = Employee()
# rohan.language = "javascript"
# print(rohan.salary,rohan.language)

# ''' Here name is object attributes and
# salary,language are class attributes as 
# they belong to the class '''


# # Constructor
# class Employee:
#     language = "python"
#     salary = 1200
    
#     def __init__(self):    # Dunder method is automatically called
#         print("I am creating an object")
        
#     def getInfo(self):
#         print(f"The language is {self.language}. The salary is {self.salary}")
        
#     @staticmethod
#     def greet():
#         print("Good Morning")
        
# harry = Employee()
# harry.name = "Harry"
# print(harry.name, harry.salary)


# # Practice set
# class Programmer:
#     company = "Microsoft"
#     def __init__(self, name, salary, pin):
#         self.name = name
#         self.salary = salary
#         self.pin = pin
        

# p = Programmer("harry", 120000, 245001)
# print(p.name, p.pin, p.company)
# r = Programmer("Rohan", 130000, 245001)
# print(r.name, r.pin, r.company)


# # Calculattor
# class Calculattor:
#     def __init__(self, n):
#         self.n = n
        
#     def square(self):
#         print(f"The square is {self.n*self.n}")
#     def cube(self):
#         print(f"The cube is {self.n*self.n*self.n}")
#     def squareroot(self):
#         print(f"The square is {self.n**1/2}")

# a = Calculattor(4)
# a.square()
# a.cube()
# a.squareroot()


# class Demo:
#     a = 4

# o = Demo()
# print(o.a)
# o.a = 0
# print(o.a)


# Calculattor
# class Calculattor:
#     def __init__(self, n):
#         self.n = n
        
#     def square(self):
#         print(f"The square is {self.n*self.n}")
#     def cube(self):
#         print(f"The cube is {self.n*self.n*self.n}")
#     def squareroot(self):
#         print(f"The square is {self.n**1/2}")
    
#     @staticmethod
#     def hello():
#         print("Hello World")

# a = Calculattor(4)
# a.square()
# a.cube()
# a.squareroot()
# a.hello()


# import random

# class Train:
    
#     def __init__(self, TrainNo):  # In place of self you can write any thing output will cant change.For ex- slf
#         self.TrainNo = TrainNo
        
#     def book(self, fro, to):
#         print(f"Ticket is book in train no. {self.TrainNo} from {fro} to {to}.")
        
#     def getStatus(self):
#         print(f"Train No. {self.TrainNo} is running on time.")
    
#     def getFare(self, fro, to):
#         print(f"Ticket fare in train no. {self.TrainNo} from {fro} to {to} is {random.randint(222, 5555).}")

# t = Train(12399)
# t.book("Silchar", "Patna")
# t.getStatus()
# t.getFare("Silchar", "Patna")

