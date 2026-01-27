# def square(n):
#     return n*n

# # Can be also written as
# # square = lambda X: X*X
# print(square(5))

# # Joint Method
# a = ["Harry", "Rohan", "Shubham"]
# final = "::".join(a)
# print(final)


# a = "{1} is a good {0}".format("harry", "boy")
# print(a)


# # Map Example 
l = [1,2,3,4,5,6]
# square = lambda x: x*X
# sqlist = map(square, l)
# print(sqlist,l)


# # Filter Example
# def even(n):
#     if (n%2==0):
#         return True
#     return False
    
# onlyEven = filter(even, l)
# print(list(onlyEven))


# # Reduce Function
# from functools import reduce 
# def sum(a,b):
#     return a+b
    
# mul = lambda x,y: x*y

# print(reduce(mul, l))
# print(reduce(sum, l))


# # Practice Set
# name = (input("Enter name: "))
# marks = int(input("Enter marks: "))
# phone = int(input("Enter phone: "))

# s = "The name of student is {}, his marks is {} and phone no. is {}".format(name, marks,phone)
# print(s)


# def divisible5(n):
#     if(n%5 == 0):
#         return True
#     return False
    
# a = [1,3,45,667,5650,34545]
# f = list(filter(divisible5, a))
# print(f)



# from functools import reduce
# l  = [223,5656,565,782,9454]

# def greater(a,b):
#     if(a>b):
#         return a
#     return b
    
# print(reduce(greater, l))



# # Flask
# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return "Hello, World!"

# app.run(debug=True)


