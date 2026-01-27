s = 'coffee'
t = 'bread'
print(t)
print(s)
# print(s+t)
# print(t + s)
# print(s[3:5])
# s = '0123456789'
# a = int(s[3])
# b = int(s[5])
# print(a)
# print(b)
# print(a+b)
# s  = 'good'
# print(s*5)
# print(s[1]*5)
# x = 'India'
# print(x == 'India')
# print(x == 'india')
# print('apple' > 'one')
# print('four' < 'ten')
# s = 'python'
# print(s[-1])
# print(s[-2])
# print(s[-3])
# print(s[-4])
# print(s[-5])
# print(s[-6])
# print(s[0])
# print(s[1])
# print(s[2])
# print(s[3])
# print(s[4])
# print(s[5])
# print(len(s))

# #String Method
# '''(1). lower() - Convert the string into lower case'''
# x = 'pytHoN sTrIng mEthOds'
# print(x.lower())

# '''(2). upper() - Convert a string into upper case'''
# x = 'pytHoN sTrIng mEthOds'
# print(x.upper())

# '''(3). capitalize() - Convert the first character to upper case'''
# x = 'pytHoN sTrIng mEthOds'
# print(x.capitalize())

# '''(4). title() - Convert the first chracter of each word to upper case'''
# x = 'pytHoN sTrIng mEthOds'
# print(x.title())

# '''(5). swapcase() - Swapcase, lower case become upper case and vice versa '''
# x = 'pytHoN sTrIng mEthOds'
# print(x.swapcase())

# # Method of checking 
# '''(1) islower() - Return true if all characters in the strings are lower case'''
# x = 'python'
# print(x.islower())
# x = 'Python'
# print(x.islower())

# '''(2) is upper() - Return true if all characters are in the string are upper case'''
# x = 'PYTHON'
# print(x.isupper())
# x = 'Python'
# print(x.isupper())

# '''(3) istitle() - Return true if the string follow the rule of a title'''
# x = 'Python String Methods'
# print(x.istitle())
# x = 'pytHoN sTrIng mEthOds'
# print(x.istitle())

# '''(4) isdigit() - Return true if all characters in the string are digits'''
# x = '123'
# print(x.isdigit())
# x = '123abc'
# print(x.isdigit())

'''(5) isalpha() - Return true if all characters in the string are in alphabets'''
# x = 'abcd'
# print(x.isalpha())
# x = 'abcd123'
# print(x.isalpha())

# '''(6) isalnum() - Return true if all character in the string are alpha-numeric'''
# x = 'abc123def'
# print(x.isalnum())
# x = '123@#$ahxj'
# print(x.isalnum())

# '''(7) strip() - Return a trimmed version of the string'''
x = '-----python-----'
# print(x.strip('-'))
# print(type(x))

# '''(8) lstrip() - Return a left trim version of the string'''
# x = '-----python-----'
# print(x.lstrip('-'))

# '''(9) rstrip() - Return a right trim version of the string'''
# x = '------python--------'
# print(x.rstrip('-'))

# '''(10) startswith() - Return true if the string start with the specified value'''
# x = 'Python'
# print(x.startswith('P'))

# '''(11) endswith() - Return true if the string ends with the specified value'''
# x = 'python'
# print(x.endswith('N'))

# '''(12) count() - Return the number of times a specified value occur in a string'''
# x = 'Python string method'
# print(x.count('t'))

# '''(13) index() - Search the string for a specified value and return the position where it was found'''
# x = 'Hello, Niranjan how are you?'
# print(x.index('r'))

# '''(14) replace() - Return a string where a specified value is replaced with a specific value'''
# x = 'hello, niranjan how are you?'
# x = x.replace('h','H')
# x = x.replace('n','N')
# print(x)

#LECTURE - 20(YOUTUBE) WEEK - 2

#This is popularly called the Caesar Cipher in Cryptography
alpha = 'abcdefghijklmnopqrstuvwxyz'
# i=20
# #print(alpha[i])
# #print(alpha[i+1])
# print(alpha[i%26])
# print(20%26)

s = 'niranjan'
# I expect to output ojsbokbo (one letter shift of given word)
t = ''
i = 0
k = 3
t =  t+( alpha[((alpha.index(s[i])+k)%26)] )
t =  t+( alpha[((alpha.index(s[i+1])+k)%26)] )
t =  t+( alpha[((alpha.index(s[i+2])+k)%26)] )
t =  t+( alpha[((alpha.index(s[i+3])+k)%26)] )
t =  t+( alpha[((alpha.index(s[i+4])+k)%26)] )
t =  t+( alpha[((alpha.index(s[i+5])+k)%26)] )
t =  t+( alpha[((alpha.index(s[i+6])+k)%26)] )
t =  t+( alpha[((alpha.index(s[i+7])+k)%26)] )
print(t)