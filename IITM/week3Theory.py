# print("when did India get independent(year)?")
# year = int(input())
# while(year!=1947):
#     print("you got this wrong. Enter once again.")
#     year = int(input())
# print("wowwwww... you got it right!")



#Lets us find the factorial of a number
# n = int(input("Enter a number: "))
#5! = 5*4*3*2*1
# factorial = 1
# factorial = factorial*2
# factorial = factorial*3
# factorial = factorial*4
# factorial = factorial*5
# print(factorial)

#n! = n*n-1*n-2*n-3*n-4*.........
#for n number of factorial it is difficult to write n times
#so, for avoiding this we use while loop
# i = 1
# factorial = 1
# while(i<=n):
#     factorial = factorial * i
#     i=i+1
# print("Factorial of number",n,"is",factorial)

# num = int(input("Enter the number: "))
# fact = 1
# if(num < 0):
#     print("not define")
# else:
#     while(num > 0):
#        fact *= num
#        num-=1    # another option here is initilise i = 1 and increase i by 1
#     print(fact)
    

#Finding digit of a number
# num = abs(int(input("Enter the number: ")))
# digit = 1
# while(num > 9):
#     num = num // 10
#     digit+=1
# print(digit)

#Let try to understand the above code 
#let user enter num = -1235 but computer understand only 1235 
#because abs means absolute value, so the negative sign is ignored, and num becomes 1235.
#initially digit = 1 counting start
#now while loop check the condition num > 9 - yes
#next num = 1235 // 10 - it return integer value 123 which is stored in num
#now digit is incremented by 1 and it become 2
#again check the condition 123>9 - yes
#num = 123//10 - it return 12 which is stored in num
#again digit is increased by 1 and it become 3
#again check the condition 12>9 - yes
#num = 12//10 - it return 1 which is stored in num
#again digit increased and it become 4
#again check the condition 1>9 which is false the code terminate here 
#and print the digit which is 4


#Reversing of a number
# num = int(input("Enter a number: "))
# absNum = abs(num)     #For negative value
# if(num >= 0):
#     rev = num % 10
#     num = num // 10
#     while(num>0):
#         r = num % 10
#         num = num // 10
#         rev = rev * 10 + r
#     print(rev)
# else:
#     rev = absNum % 10
#     absNum = absNum // 10
#     while(absNum>0):
#         r = absNum % 10
#         absNum = absNum // 10
#         rev = rev * 10 + r
#     print(rev - 2 *rev)  #why? because else statement is also work for positive


    
#IN SHORT
# num = int(input("Enter a number: "))
# absNum = abs(num)
# rev = absNum % 10
# absNum = absNum // 10
# while(absNum > 0):
#     r = absNum % 10
#     absNum = absNum // 10
#     rev = rev * 10 + r
# if(num>=0):    
#     print(rev)
# else:
#     print(rev - 2 *rev)
    

#Palindrome 

num = int(input('Enter a number: '))
#fistly, user give the input let -12321 this number stored in num
#num = -12321
absNum = abs(num)
#abs means absolute value it remove the sign and take absolute value i.e. 12321
#now absNum = 12321
rev = absNum % 10
#rev = 12321 % 10 - it give the remainder 1 and stored in rev
#rev = 1
absNum = absNum // 10
#absNum = 12321 // 10 - here, integer division occur 
#now absNum = 1232
while(absNum > 0):
    r = absNum % 10
    absNum = absNum // 10
    rev = rev * 10 + r
#while loop check the condition absNum > 0 (1232>0) if yes then exucate the next line
#new variable r = 1232 % 10 - it give the remainder 2
#now r = 2 next line absNum = 1232 // 10 - it give the value 123
#now absNum = 123 next line execute rev = rev * 10 + r
#now rev = 1 * 10 + 2 = 12
#again while loop check the condition absNum > 0 (123>0) yes the next line execute
#r = 123 % 10 - it return 3 now r = 3
#absNum = 123 // 10 - it return 12 now absNum = 12
#rev = 12 * 10 + 3 = 123, now rev = 123 
#again while loop check the condition absNum > 0 (12>0) yes the next line execute
#r = 12 % 10 - it return 2 now r = 2
#absNum = 12 // 10 - it return 1 now absNum = 1
#rev = 123 * 10 + 2 = 123, now rev = 1232
#again while loop check the condition absNum > 0 (1>0) yes the next line execute
#r = 1 % 10 - it return 3 now r = 1
#absNum = 1 // 10 - it return 0 now absNum = 0
#rev = 1232 * 10 + 1 = 12321, now rev = 12321
# again while loop check the condition absNum > 0 (0>0) no the next line not execute
#while loop terminate  and move net line of code  
if(num<0):
    rev = rev - 2 *rev
#also checking for negative value 
if(num == rev):
    print('palindrome')
#now value of rev = 12321, if num = rev then if block print the palidrome
else:
    print('not palidrome')
#if num not equal to rev then else block print not palidrome