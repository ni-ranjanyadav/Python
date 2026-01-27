# def add(a, b):
#     ans =a + b
#     print(ans)

# add(9, 90)
# add(5656, 5545)

# def discount(cost,d):
#     ans = cost - (cost*(d/100))
#     print(ans)
# discount(2900,30)


# def add(a,b):
#     ans = a+b
#     return ans

# a = 2
# b = 15
# sum = add(45,65) + 20
# print(sum)

# def discount(cost,d):
#     ans = cost-(cost*(d/100))
#     return ans
# print("Enter the cost price: ")
# x = int(input())
# print("Enter the discount: ")
# y = int(input())
# print("The final price is: ",discount(x,y))

# def list_min(l):  # Define function
#     mini = l[0]  # Let first element is min
#     for i in range(len(l)):  # Check full list
#         if(l[i] < mini):  # If any less than l[0] then store in mini
#             mini = l[i]
#     return mini

# l = [1,2,3,4,5,-12,34,7]
# print(list_min(l))

# def list_max(l):
#     maxi = l[0]
#     for i in range(len(l)):
#         if (l[i]>maxi):
#             maxi = l[i]
#     return maxi

# l = [45,65,8,64,56,9]
# print(list_max(l))


# # LIST PREFIX (APPEND BEFORE)
# def list_appendbefore(l,z):
#     new_list = []
#     for i in range (len(z)):
#         new_list.append(z[i])
#     for i in range (len(l)):
#         new_list.append(l[i])
#     return new_list

# def list_appendend(l,z):
#     new_list = []
#     for i in range (len(l)):
#         new_list.append(l[i])
#     for i in range (len(z)):
#         new_list.append(z[i])
#     return new_list

# l = [15,83,56,6,4,64,64,78]
# z = [54,5,99,46,9,7,45,6,659]
# print(list_appendbefore(l,z))
# print(list_appendend(l,z))

# # AVERAGE OF A NUMBER
# def list_average(l):
#     sum = 0
#     for i in range(len(l)):
#         sum = sum + l[i]
#         average = sum/len(l)
#     return average

# l =[1,7,8,10]
# print(list_average(l))


# Type of function
# 1. Inbult function
# print(),input(),len()

# 2. Library function
# math.log(), math.squrt(), random.random(), randrange(), calender(), calender.month()

# 3. String method (function)
# upper(), lower(), strip(), count(), index(), replace()

# 4. User defined function
# def square(x):
#     squr = x**2
#     return squr

# print(square(5))

