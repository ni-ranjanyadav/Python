# word1, word2 are two strings
# word1 = 'niranjan'
# word2 = 'yadav'
# print(word1 + word2)
# word = word1
# word1 = word2
# word2 = word
# print(word2 + word1)

# a = 4.235
# print(int(-a))

# a = 8
# b = 10
# c = 3
# x,y,z = 4,2,3
# x=y=z
# print(bool(x==y==b))


# flag = True
# if flag == True:
#     print('works')

# flag = True
# if flag:
#     print('works')
    

# if False:             # In Python if- statement only work when it is True.
#     print('good')
# else:
#     print('bad')

# if True:
#     print('good')
# print('bad')

# print('good')
# print('bad')


# bool_var = True               # Here, bool_var is True                              # If bool_var is False
# x =10                         # value of x = 10                                     # value of x = 10
# if bool_var:                  # bool_var is True so, if part is executed            # if part is not executed and this outside if has not else 
#     x = x + 1                 # x = 10+1 = 11, value of x become 11                 # so, directly print the value of x = 10
#     bool_var = not bool_var   # True = not True (i.e. False) means bool_var = False
#     if bool_var:              # Now if part is False, then else part execute
#         x = x + 1             # This line not execute
#     else:                     # else part is execute because of false
#         x = x - 1             # x = 11-1 = 10, Now value of x become 10
# print(x)                      # print x = 10


# E_1 = False
# E_2 = False
# E_3 = False
# if E_1:
#     x = 1
# if E_2:
#     x = 2
# if E_3:
#     x = 3
# print(x)


print("\\\\")


a, b, c, d = input()
print(a)
print(b)
print(c)
print(d)

alphabets = 'abcdefghijklmnopqrstuvwxyz'
even = alphabets[0: 10: 2]
print(even)