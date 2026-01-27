# def avg():
#     a = int(input("Enter a number: "))
#     b = int(input("Enter a number: "))
#     c = int(input("Enter a number: "))
#     average = a+b+c/3
#     print(average)
    
# avg()


def GoodDay():
    print("Good Day!")
GoodDay()


# Recursion

# def factorial(n):
#     if(n==1 or n==0):
#         return 1
#     return n * factorial(n-1)
    
# n = int(input("Enter a number: "))
# print(f"The factorial of {n} is {factorial(n)}")



# Practice set

# def gratest(a,b,c):
#     if(a>b and a>c):
#         return a
#     elif(b>a and b>c):
#         return b
#     elif(c>a and c>b):
#         return c 
    
# a = 1
# b = 56
# c = 34
# print(gratest(a, b, c))

# def f_to_c(f):
#     return 5*(f-32)/9

# f = int(input("Enter temperature in F : "))
# print(f"{round(f_to_c(f), 2)}C")  # round at 2 digit

# print("a")
# print("b")
# print("c", end="")
# print("d", end="")


# def sum(n):
#     if(n==1):
#         return 1
#     return sum(n-1) + n
    
# n = int(input("Enter a number: "))
# print(sum(n))


# def pattern(n):
#     if(n==0):
#         return 
#     print("*" * n)
#     pattern(n-1)

# pattern(5)


# def rem(l, word):
#     n = []
#     for item in l:
#         if not(item == word):
#             n.append(item.strip(word))
#     return n
        
# l = ["niranjan", "yadav", "an"]
# print(rem(l, "an"))


def multiply(n):
    for i in range(1, 11):
        print(f"{n} X {i} = {n*i}")

n = int(input("Enter any number: "))
print(multiply(n))