# class Two_D_vector:
#     def __init__(self, i, j):
#         self.i = i
#         self.j = j 
        
#     def show(self):
#         print(f"The vector is {self.i}i + {self.j}j")
        
# class Three_D_Vector(Two_D_vector):
#     def __init__(self, i, j, k):
#         super().__init__(i, j)
#         self.k = k 
    
#     def show(self):
#         print(f"The vector is {self.i}i + {self.j}j + {self.k}k")
        
# a = Two_D_vector(1, 2)
# a.show()

# b = Three_D_Vector(1, 2, 3)
# b.show()



# # Problem - 02
# class Animals:
#     pass
    
# class Pets(Animals):
#     pass
    
# class Dog(Pets):
    
#     @staticmethod
#     def bark():
#         print("boww bow!")
        
# d = Dog()
# d.bark()


# # Problem - 3
# class Employee:
#     salary = 234
#     increment = 20
    
#     @property
#     def salaryAfterIncrement(self):
#         return (self.salary + self.salary * (self.increment/100))
        
# e  = Employee()
# print(e.salaryAfterIncrement)


# class Complex:
#     def __init__(self, r, i):
#         self.r = r
#         self.i = i
        
#     def __add__(self, c2):
#         return Complex(self.r + c2.r, self.i + c2.i)
        
#     def __str__(self):
#         return f"{self.r} + {self.i}i"
        
# c1 = complex(1, 2)
# c2 = complex(3, 4)
# print(c1 + c2)


