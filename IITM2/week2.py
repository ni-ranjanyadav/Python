# a_ = 'Hi, This is Niranjan.'
# _a = 7
# a_variable = 'Hello, How are you?'
# print(a_, _a, a_variable, sep=",")

# word1 = "Niranjan"
# word2 = " Yadav"
# print(word1 + word2)

# word = word1
# word1 = word2
# word2 = word
# print(word2 + word1)

# a = 2
# b = 3
# c = 4
# x,y,z = a,b,c
# x=y=z
# print(x,y,z)

# flag = True 
# if flag == True:
#     print('works')

# flag = True
# if flag:
#     print('works')


# bool_var = True
# x = 50
# if bool_var:
#     x = x + 1
# bool_var = not bool_var
# if bool_var:
#     x = x + 1
# else:
#     x = x - 1
# print(x)

# print('\\')
# print("A single quote ' and a double quote \" ")
# print("A forward slash / and a backward slash \\")
# print("Three single quotes ''' and three double quotes \"\"\"")
# print("Double forward slash // and Double backward slash \\\\")

# word  = "glow"
# continuous_tense = True
# new_word = word
# if 'ing' in new_word:
#     new_word = new_word[0:-3]
#     # we have to remove last three word 

# if new_word != 'ing' and continuous_tense == True:
#     new_word = new_word + 'ing'
# else:
#     new_word = new_word

# age = 5
# is_member = True

# if age >= 18:
#     age_group = 'Adult'
# else:
#     age_group = 'Child'

# if is_member == True and age_group == 'Adult':
#     applicant_type = "Adult Member"
# elif is_member == True and age < 18:
#     applicant_type = "Adult Non-Member"
# elif is_member == False and age_group == 'Child':
#     applicant_type = "Child Member"
# else:
#     applicant_type = "Child Non-Member"

# time = "02 PM"
# parts = time.split()
# print(parts)
# hour = int(parts[0])
# period = parts[1]
# print(hour)
# print(period)
# is_time_valid = True if 1 <= hour <= 12 else False
# print(is_time_valid)
# time_in_hrs = 0 if period == 'AM' and hour == 12 else (hour if period == 'AM' else (12 if hour == 12 else hour + 12))
# # This can be also written as
# if period == "AM":
#     if hour == 12:
#         time_in_hrs = 0
#     else:
#         time_in_hrs = hour
# else:  # PM
#     if hour == 12:
#         time_in_hrs = 12
#     else:
#         time_in_hrs = hour + 12

'''strip() is a Python string method
 that removes unwanted characters 
 from the beginning and end of a string.'''

"""format specifiers
print(f"{500:06}")
print(f"{500:06f}")

:06 0 → pad with zeros
    6 → total width should be 6 characters
:06f
f → floating-point format
Default precision = 6 digits after the decimal point
6 → minimum field width is 6"""

# s1 = f"{0.5}00"
# print(s1)
# s2 = f"{0.545:.1f}"
# print(s2)
#.1f means display 1 digit after the decimal point.
# 0.545 is rounded to 1 decimal place.

# import keyword
# print(keyword.kwlist)

# print(5 and 3)
# print(5 & 3) 
''' &(and),|(or),^(xor),~(not) these are bitwise operator
  first convert it into binary then compare every bits
 '''
# #Raw string
# print(r'C:\Users\Niranjan kumar\OneDrive\Desktop\Python')
# #If you can't use raw string then use \\ backward slash to print single slash
# print('C:\\Users\\Niranjan kumar\\OneDrive\\Desktop\\Python')
# print('My name is \"NIRANJAN YADAV\".Currently I\'m learning python.')

'''
String Method
.upper()
.lower()
.capatilize()
.swapcase() In swapcase smaller letter change into capital letter and vise versa
.title()
.strip() remove extra space or other char before or after the word
.replace()
.find()
.count()
.startswith("")
.endswith("")
.split(" ") it split the string by ,(comma) or other 
" ".join()
isalpha()
isalnum()
isdigit()
'''

# x, y, z = '123'
# print(x)
# print(y)
# print(z)
# print(x,y,z)
# print(f"{5:9}")
# print(f"{5:^9}")
# print(f"{5:>9}")
# print(f"{5:<9}")
# a,b = '56'
# s = f'{a*3:9}|{b*5:^9}|{a*7:>9}'
# print(s)
# print(0.0 or "2" or 4)
# print("2" and 4 and None) # None is Falsy

# a = 4
# b = 0
# c = 4
# if a:
#   print('a') 
#   if b:
#     print('b') 
#   elif c:
#     print('c')

# from math import pi as math_pi
# x = 2*math_pi*5
# print(x)


# dept = input() 
# course = input() 
# prefix = input() 
# name = input() 
# roll_no = input() 
# name = prefix + " " + name.upper() # one space 
# lib_id = dept[0] + course[0] + roll_no 
# print("Student record:") 
# indent = ' ' # four spaces 
# print(indent + "Dept:", dept) 
# print(indent + "Name:", name) 
# print(indent + "Roll No:", roll_no) 
# print(indent + "Library Card No:", lib_id)

# # L is a positive integer that has already been defined at this stage
# L = int(input())
# word = input() 
# space = ' ' # there is a single space 
# if len(word) < L: 
#   word = 'short' + space + word 
# elif L <= len(word) < 2 * L: 
#   word = 'medium' + space + word 
# else: word = 'long' + space + word 
# print(word)

# num = input()
# first = int(num[0])
# middle = int(num[1])
# last = int(num[2])
# if first + last == middle:
#   print('sandwich')
# else:
#   print('plain')

# a = int(input()) 
# b = int(input()) 
# if a > 0: 
#   if b < 0: 
#     print('OK')

# if int(input()) > 0 and int(input()) < 0: print('OK')

# a = "Alex"
# b = "alex"
# if id(a) == id(b):
#   print("Both have same memory location.",id(a),id(b))
# else:
#   print("Both have not same memory location.",id(a),id(b))

# x = 1
# while((x**2 + x + 41) % 41 != 0):
#   x += 1
#   print(x)