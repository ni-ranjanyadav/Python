# s = 'VIBGYOR'
# for i in range(7):
#     print(s[i])
    

# num = int(input("Enter the number: "))
# if(num > 2):
#     print(2, end = ' ')
# for i in range(3,num):
#     flag = False
#     for j in range(2, i):
#         if(i % j == 0):
#             flag = False
#             break
#         else:
#             flag = True
#     if(flag):
#         print(i, end =  ' ')
        

# empID = input('Enter employee ID: ')
# while(empID != '-1'):
#     trade = int(input('Enter the trade amount: '))
#     profit_loss = 0
#     while(trade != 0):
#         profit_loss = profit_loss + trade
#         trade = int(input('Enter the trade amount: '))
#     print(f'Profit/loss for employee {empID} is {profit_loss}')
#     empID = input('\nEnter employee ID: ')
    

# days = int(input('Enter the no of days: '))
# for i in range(1, days+1):
#     total = 0
#     rainfall = int(input('Enter the rainfall: '))
#     while(rainfall != -1):
#         total = total + rainfall
#         rainfall = int(input('Enter the rainfall: '))
#     print('total rainfall for days {0} is {1}'.format(i,total))
    
    
# word = input('Enter a word: ')
# maxlen = 0
# while(word != '-1'):
#     count = 0
#     for letter in word:
#         count = count + 1
#     if(count > maxlen):
#         maxlen = count
#     word = input('Enter a word: ')
# print("The length of longest word is %s" %maxlen)


#Break, Continue, Pass

# email = input()
# for c in email:
#     if(c == '@'):
#         break
#     print(c, end = '')
    
# email = input()
# for c in email:
#     if(c == '@'):
#         print('')
#         continue
#     print(c, end = '')
    

for x in range(11):
    if(x%3==0):
        print(x, end = ' ')
    else:
        pass
# pass is nothing but if we don't know what i will write 
# in else statement then we simply write pass  