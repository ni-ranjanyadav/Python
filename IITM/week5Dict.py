# d = {}
# d['sudarshan'] = 9858367415
# d['niranjan'] = 9656548798
# d['aryan'] = 9865656565
# print(d)


# d = {'key': 'value'}
# d = {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
# print(d)
# for key in d:
#     print(key, d[key])
    
# d = {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
# print(d.keys())
# print(d.values())
# print(d.items())


# n = int(input('Enter value of n: '))
# a = 0
# for i in range(1, n + 1): 
#     b = 1
#     for j in range(1, i + 1):        
#         b = b * j
#     a = a + b
# print(a)


# b = 200
# x = 0
# while True:
#     if x < 10:
#         x = int(input())
#         continue
#     elif b < x < b + 2:
#         break
#     print(b)
    

# def obvious_sort(l):
#     x = []
#     while(len(l)>0):
#         mini = l[0]
#         for i in range(len(l)):
#             if l[i] < mini:
#                 mini  = l[i]
#         x.append(mini)
#         l.remove(mini)
#     return x

# l = [21,88,65,8,56,54,7,94]
# print(obvious_sort(l))


# r1 = [1,2,3]
# r2 = [4,5,6]
# r3 = [7,8,9]

# s1 = [1,2,1]
# s2 = [6,2,3]
# s3 = [4,2,1]

# A = []
# B = []
# A.append(r1)
# A.append(r2)
# A.append(r3)

# B.append(s1)
# B.append(s2)
# B.append(s3)

# C = [[0,0,0],[0,0,0],[0,0,0]]

# dim = 3

# # C[2][1] IS THE DOT PRODUCT OF THE 2ND ROW OF A 
# # AND THE 1ST COLUMN OF B
# for i in range(dim):
#     for j in range(dim):
#         for k in range(dim):
#             C[i][j] = C[i][j]+A[i][k]*B[k][j]
# print(C)


# import numpy as np
# A = [[1,2,3], [4,5,6], [7,8,9]]
# B = [[1,2,1], [6,2,3], [4,2,1]]
# x = np.array(A)
# y = np.array(B)
# print(x@y)  


# def myFunction():         # Declear a function
#     global x
#     x  = x*2               # variable x which store value after operation
#     print("Value of function ", x)  # Print statement which print value of x

# def myFunction1():
#     global x
#     x = x*3
#     print("value of x in function1", x)

# x = 5        # Now we declear value of x is 5
# print("Value of x before function call",x) # This print statement print the value of x = 5
# myFunction() # Here we call a function so, x = 5 goes into the function and x =5*2 = 10 
# myFunction1()
# # and next print statement print the valu of x whih is 10
# print("value of x after function call ",x)  # This print statement is independent from function so, it print x = 5

# A = [[1,2,3],[4,5,6],[7,8,9]]
# B = [[4,5,6],[1,4,7],[3,6,9]]
# import numpy
# A = numpy.array(A)
# B = numpy.array(B)
# C = A*B
# print(C)


# def some_function(word):
#     space = ' ' # there is a single space between the quotes
#     if space in word:
#         return False
#     # both letters 'A' and 'Z' are in upper case
#     if not('A' <= word[0] <= 'Z'):
#         return False
#     for i in range(1, len(word)):
#         # both letters 'a' and 'z' are in lower case
#         if not('a' <= word[i] <= 'z'):
#             return False
#     return True



# def upper(s):
#     upper = 0
#     for c in s:
#         if (c.isupper()):
#             upper += 1
#     return(upper)

# def lower(s):
#     lower = 0
#     for c in s:
#         if (c.islower()):
#             lower += 1
#     return(lower)

# def characters(s):
#     characters = 0
#     for c in s:
#         characters += 1
#     return(characters)
    
# def word(s):
#     words = 0
#     for c in s:
#         if(c == ' '):
#             word += 1
#     return(words)

# sentence = input('Enter the sentence:')
# UpperLetter = upper(sentence)
# lowerletter = lower(sentence)
# char = characters(sentence)
# print(f'\n Total number of lower case char: {lowerletter}')
# print(f'\n Total number of upper case char: {UpperLetter}')
# print(f'\n Total number of char: {char}')


# we have to find the area of a circle and rectangle
# Approach 1:Standard code 
# pi = 22/7
# def circle_area(r):
#     return (pi*r*r)

# def circle_perimeter(r):
#     return (2*pi*r)

# def rectangle_area(l,b):
#     return (l*b)

# def rectangle_perimeter(l,b):
#     return (2*(l*b))

# r = float(input("Enter the radius of the circle: "))
# C_area = circle_area(r)
# print(f'Area of circle with radius {r} is = {C_area} sq. unit.')
# C_perimeter = circle_perimeter(r)
# print(f'Perimeter of circle with radius {r} is {C_perimeter}.')

# l = float(input("Enter the length of a rectangle: "))
# b = float(input("Enter the breadth of a rectangle: "))
# R_area = rectangle_area(l,b)
# print(f'Area of rectangle with length {l} and breadth {b} is {R_area}.')
# R_perimeter = (f'Perimeter of rectangle with length {l} and breadth {b} is {R_area}.')

# # Approach 2: Menu driven code
# import math
# pi = math.pi
# def circle_area(r):
#     return (pi*r*r)

# def circle_perimeter(r):
#     return (2*pi*r)

# def rectangle_area(l,b):
#     return (l*b)

# def rectangle_perimeter(l,b):
#     return (2*(l*b))

# polygon = ''
# while(polygon != 'exist'):
#     print('\nPOLYGONS\ncircle\nrectangle\nexist')
#     polygon = input('Choose the polygon type or exist: \n')
#     property = ''
#     if(polygon == 'circle'):
#         r = float(input("\nEnter the radius of circle: "))
#         while(property == ""):
#             print("\nCIRCLE PROPERTIES\narea\nperimeter\nback")
#             property = input('\nChoose the circle propertyor go back: ')
#             if(property == 'area'):
#                 C_area = circle_area(r)
#                 print(f'Area of circle with radius {r} is = {C_area} sq. unit.')
#             elif(property == 'perimeter'):
#                 C_perimeter = circle_perimeter(r)
#                 print(f'Perimeter of circle with radius {r} is {C_perimeter}.')
#             elif(property == "back"):
#                 break
#             else:
#                 print('please select the correct polygon property')
#                 property = ''
#     elif(polygon == 'rectangle'):
#         l = float(input('Enter the length of the rectangle: '))
#         b = float(input('Enter the breadth of the rectangle: '))
#         while(property == ''):
#             print('\nRECTANGLE PROPERTIES\narea\nperimeter\nback')
#             property = input('\nChoose the rectangle property or go back: ')
#             if(property == 'area'):
#                 R_area = rectangle_area(l,b)
#                 print(f'Area of rectangle with length {l} and breadth {b} is = {R_area} sq. unit.')
#             elif(property == 'perimeter'):
#                 R_perimeter = rectangle_perimeter(l,b)
#                 print(f'Perimeter of rectangle with length {l} and breadth {b} is {R_perimeter}.')
#             elif(property == "back"):
#                 break
#             else:
#                 print('please select the correct polygon property')
#                 property = ''
#     elif(polygon == 'exist'):
#         break
#     else:
#         print('Please select the correct polygon type or exist')  
        
        
# # Iterator and Genrator
# def square(limit):
#     x = 0
#     while x < limit:
#         yield x * x
#         yield x * x * x
#         x += 1

# a = square(5)
# print(next(a),next(a))
# print(next(a),next(a))
# print(next(a),next(a))


# # Lambda Function
# def add(x,y):
#     return x+y

# def sub(x,y):
#     return x-y

# def mul(x,y):
#     return x*y

# def div(x,y):
#     return x/y

# add = lambda x,y: x + y
# sub = lambda x,y: x - y
# mul = lambda x,y: x * y
# div = lambda x,y: x / y
# print(add(10,20))
# print(sub(10,20))
# print(mul(10,20))
# print(div(10,20))
# print(type(add))

# fruits = ["mango", "apple", "banana", "orange", "pineapple", "watermelon", "guava", "kiwi"]
# size = [5,5,6,6,9,10,5,4]
# print(dict(zip(fruits, size)))
# print(list(zip(fruits, size)))

# a = [10,20,30,40,50]
# b = [5,10,15,20,25,]

# def sub(x,y):
#     return x - y

# c = map(sub,a,b)
# print(list(c))



# l = [2,3,4,5,5]
# print(type(l))
# x = sorted(l)
# print(type(x))
# l1 = l + [5]
# print(type(l1))
# l2 = l.append([5])
# print(type(l2))
# l5 = l[:2]
# print(type(l5))
# l = ['a','b','c','hi']
# print(type(l.index('hi')))
# print(type(l.remove('hi')))
# print(type(l.pop()))
# l = []
# print(type(l))
t = (3,4,5)
print(type(t))
# t1 = t+(5,6)
# print(type(t1))
# s = {2,3,4,5,8,8,7,9,4,4,5,5,5}
# print(type(s.pop()))
# print(type(s))
# print(type(s.add((1,2))))
# print(type(s^s))
# print(type(s.update({1,2})))
# d = {'a': 1}
# print(type(d))