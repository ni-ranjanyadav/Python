# for i in range(10):
#     print('Hello, India')
#i takes the value in the range[0,9]

#An example of for loop
# for i in range(12):
#     print(i, "Hello, india")
#     print(i,'niranjan yadav')
    
#Add the first 10 integers
#0+1+2+3+4+5+6+7+8+9 = 45
# n = int(input('Enter no of term:'))
# sum = 0
# for i in range(n):   #i take the value from 0 to (n-1)
#     sum = sum + i
# print(sum)


#Multiplication of number and different type of a print statement
# for i in range(1,11):
    # print("2 X", i, "=",2*i)
    # print(f'{2} X {i} = {2 * i}')
    # print('{0} X {1} = {2}'.format(2, i, 2*i))
    # print('%d X %d = %d' % (2, i, 2*i))
    
# #Odd number b/w 0 and 100
# for x  in range(0,100):
#     if(x % 2 != 0):
#         print(x)
        
# #Alternate method
# for x in range(0,100,2):
#     print(x)
  
  
# for x in range(100,-1,-2):
#     print(x)
#Their output can be printed in one line by using end statement
# for x in range(100,-1,-2):
#     print(x, end = ' ')
    
    
# country = "India"
# for letter in country:
#     print(letter, end = " ")
    
    
# ##Separator 
# d = 9
# m = 10
# y = 2025
# print("Today's date is", d, m, y, sep = '/')

# pi = 22/7
# print('value of pi =',pi)
# print(f'value of pi = {pi:.2f}')
# print('value of pi = {0:.2f}'.format(pi))
# print('value of pi = %.2f' % (pi))

# for x in range(1, 6):
#     print(f'The square of {x} is equal to {x ** 2}')
    
# total = 0
# count = 0
# for i in range(1000):
#     if i % 2 != 0 and count <= 50:
#         total = total + i
#         count = count + 1
# average = total / count
# print(average)
# print(total)
# print(count)

# name = input()
# nick = ''    # there is no space between the quotes
# space = ' ' # there is one space between the quotes
# first_char = True
# for char in name:
#     if first_char == True:
#         nick = nick + char
#         first_char = False
#     if char == space:
#         first_char = True
# print(nick)


# n = int(input())
# F_prev = 1
# F_curr = 1
# for i in range(n - 2):
#     temp = F_prev + F_curr
#     F_prev = F_curr
#     F_curr = temp
# print(F_curr)

# n = int(input())
# F_prev = 1
# F_curr = 1
# count = 2
# while count < n:
#     temp = F_prev + F_curr
#     F_prev = F_curr
#     F_curr = temp
#     count += 1
# print(F_curr)

# n = int(input())
# F_prev = 1
# F_curr = 1
# count = 2
# while count < n:
#     temp = F_prev + F_curr
#     F_prev = F_curr
#     F_curr = temp
#     count += 1
# print(F_curr)

# n = int(input())
# F_prev = 1
# F_curr = 1
# for i in range(n):
#     temp = F_prev + F_curr
#     F_prev = F_curr
#     F_curr = temp
# print(F_curr)

# x = int(input("Enter any number: "))
# while(x % 5 != 0 and x % 10 != 0):
#     x = int(input("Enter any number: "))
# print("outside loop, the value of x is ", x)

# x = 0
# x_ = 1
# for i in range(10):
#     # x, x_ = x_, x + x_
#     X = x_
#     x_ = X + x_
# print(x)


# day = '01'
# month = '01'
# year = '2021'
# hour = '12'
# minute = 30
# second = '00'
# print(day, month, year, sep = "-", end = " ")
# print(hour, minute, second, sep =":")
# print(f"{day}-{month}-{year} {hour}:{minute}:{second}")
# print("%s-%s-%s %s:%s:%s"%(day, month, year, hour, minute, second))


# for i in 'We are in question one':
#     if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
#         continue
#     print(i, end = '')

# for i in range(10, 0, 1):
#     print(i)
    

# for i in range(10):
#     for j in range(10):
#         break
#     break

# for i in range(10, 0, -1):
#     print(i)
    
# total = 0
# for i in range(1, 5):
#     for j in range(i):
#         total = total + i
# print(total)

# word = input()
# valid = True
# for i in range(len(word)):
#     char = word[i]
#     if i % 2 == 0 and char not in 'aeiou':
#         valid = False
# print(valid)

# n = int(input())
# result = 0
# i = 0
# while i<2*n+1:
#     if i%2 != 0:
#       result+=i
#     i+=1
# print(result)

# result = 0
# for i in range(1,n):
#     result+=2*i+1
# result+=1
# print(result)

# result = 0
# for i in range(1,n):
#     result+=2*i+1
# print(result)

# result = 0
# for i in range(-1,-n-1,-1):
#     result-=2*i+1
# print(result)

# result = 0
# for i in range(-1,-n):
#     result-=2*i+1
# print(result)

# n = int(input())
# value = 0
# for i in range(n):
#     value+=int(input())*2
# print(value)

# sentence = input()
# value = ""
# for char in sentence:
#     if char in 'aeiou':
#         value+=chr(ord(char)+1)
#     else:
#         value+=chr(ord(char)-1)
# print(value)


# n = int(input())
# for i in range(n):
#   num = int(input())
#   if len(str(num))<2:
#       print(num)
      
      
# n = int(input())
# for i in range(n):
#   num = int(input())
#   if len(str(num))<2:
#       print(num)
#       break
  

# num = int(input())
# i = -num
# result = 0
# while True:
#     if i>5:
#         break
#     if i<-5:
#         continue
#     result += i
#     i += 2
# print(result)

n = int(input())
for i in range(1, n+1):
    print(i, end= "")