# a = 5                         # Value of a = 5
# b = a                         # b = a means value of b = 5
# c = "hello"                   # c = hello
# d = c[:3]                     # d become hel because c[:3] - slicing means it take value 0, 1, 2 only
# b,d = c,b                     # here b = c , d = b means  b = hello , d = hello                   
# b,e = d,b                     # here b = hello and e = hello
# d,b = e,c                     # here d = hello and b = hello
# f,d = d,e                     # f = hello and d = hello
# del e

# s = '''
# The first line.
# The second line.
# '''
# print(s)

# K = f"{0.545:.1f}00"
# print(K)


# n_apples = 5
# n_bananas = 7
# apple_price = 1.75
# m = f"{n_apples} kgs of apple cost ₹ {n_apples*apple_price:05.2f}"


#n = f"{n_apples} kgs of apple cost ₹ {n_apples*apple_price:02.2f}"


#o = f"{n_apples} kgs of apple cost ₹ {n_apples*apple_price}"


#p = f"{n_apples} kgs of apple cost ₹ {n_apples*apple_price:.2f}"


#q = n_apples+" kgs of apple cost ₹ "+n_apples*apple_price


#r = str(n_apples)+" kgs of apple cost ₹ 0"+str(n_apples*apple_price)


#s = str(n_apples)+" kgs of apple cost ₹ "+str(n_apples*apple_price)

#print(m)
#print(n)
#print(o)
#print(p)
#print(q)
#print(r)
#print(s)

# a,b = "56"
# s = f'{a*3:9}|{b*5:^9}|{a*7:>9}'
# print(s)


# s = 'xyz'
# print(type("python3".replace('h',s).index("3")))
# '''Here, .replace('h',s) - only h can replace by xyz (pytxyzon3)
# pytxyzon3 - .index("3") - it means it is asking about position of 3 in "pytxyzon3"
# so, the index of 3 is 8 and finally print the integer value 8.'''

# s = 'niranjan'
# x =s.join([s[0],s[1],s[3]])
# print(x)
# print(type(s.join([s[0],s[1],s[3]])))


x = bool(0 or "2" and 0)    #(Python logical operators have this precedence: and > or)
print(x)


# a = input()
# b = input()
# c = input()
# if a:
#   print('a')
# elif b:
#   print('b')
# else:
#   print('c')


# if a:
#   print('a')
#   if b:
#     print('b')
#     if c:
#       print('c')
      

# if a:
#     if b:
#         print('b')
#     if c:
#         print('c')
#     print('a')


# if a:
#     if b:
#         print('b')
#     if c:
#         print('c')
#     print('a')


# word = input()
# match = False
# if word.count('(') == word.count(')'):
#     if word.count('[') == word.count(']'):
#         if word.count('{') == word.count('}'):
#             match = True
# if match:
#     print('PERFECT!')
# else:
#     print('IMPERFECT!')


# s = "abcdefghijklmnopqrstuvwxyz"
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# e = int(input())
# print(s[-a:-len(s):-3])
# print(s[::-b])
# print(s[c:0:-3])
# print(s[len(s):-d:-3])
# print(s[:e:-3])
# print(s[::-b])


# The Slicing Format
# s[start:stop:step]  
# start → index where slicing starts
# stop → index where slicing ends (not included)
# step → how many indexes to move each time
# If Step is Negative
# s([::step]) - start is empty → start from the end of the string
# stop is empty → go until the beginning
# step = -2 → move backward 2 steps at a time 
# If Step is Positive
# s([::step]) - start is empty → start from the beginning of the string
# stop is empty → go until the end
# step = 2 → move forward 2 steps at a time 


# x = int(input())
# y = int(input())
# z = int(input())

# # Block-1 Start
# if x > 0 or y > 0 or z > 0:
#     if (x > 0 and y > 0) or (y > 0 and z > 0) or (z > 0 and x > 0):
#         if x > 0 and y > 0 and z > 0:
#             print('P3')
#         else:
#             print('P2')
#     else:
#         print('P1')
# # Block-1 End

# # Block-2 Start
# if x < 0 or y < 0 or z < 0:
#     if (x < 0 and y < 0) or (y < 0 and z < 0) or (z < 0 and x < 0):
#         if x < 0 and y < 0 and z < 0:
#             print('N3')
#         else:
#             print('N2')
#     else:
#         print('N1')
# # Block-2 End


a = input()
b = input()
c = input()
# if a:
#     if b:
#         print('ab')
# elif c:
#     print('c')

# if a or b:
#     print('ab')
# elif c:
#     print('c')
    
# if not (not a or not b):
#     print('ab')
# elif c:
#     print('c')

# if a:
#     if b:
#         print('ab')
# if c:
#     print('c')

# if a and b:
#     print('ab')
# elif c:
#     print('c')

# if a and b:
#     print('ab')
# if c:
#     print('ac')

# if a and b:
#     print('ab')
# if c:
#     if not(a and b):
#         print('c')

# if a and b:
#     print('ab')
# if c:
#     if not a:
#         print('c')

if a and b:
    print('ab')
if not a and c:
    print('c')
    
s = "A single quotes \' and a double quotes \""
print(s)
t = "A forward slash / and a backward slash \\"
print(t)