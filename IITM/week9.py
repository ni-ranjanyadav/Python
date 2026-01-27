# def obvious_search(L,K):
#     for x in L:
#         if x == K:
#             return 1
#     return 0

# L = list(range(100))
# #print(L)
# print(obvious_search(L,200))


import time
a = time.time()
print(a)


# #ZERO DIVISION ERROR
# a = int(input())
# b = int(input())
# try:
#     c = a/b
#     print(c)
#     f = open('abc.txt','r')
# except ZeroDivisionError:
#     print('Invaled input,divisor can not be zero')
# except NameError:
#     print('Variable not defined')
# except FileNotFoundError:
#     print('Invalid file name.Please check again')
# except:
#     print('Something went wrong.')

    
# a = int(input())
# b = int(input())
# try:
#     f = open('abc.txt','r')
#     c = a/b
#     print(c)
#     # f.close()
# except ZeroDivisionError:
#     print('Invaled input,divisor can not be zero')
# except NameError:
#     print('Variable not defined')
# except FileNotFoundError:
#     print('Invalid file name.Please check again')
# except:
#     print('Something went wrong.')
# finally:
#     f.close()
#     print('Form finally block')


a = int(input())
if a < 18:
    raise Exception('you are underage, you cant vote.')