# for i in range(100):
#     if(i == 43):
#         break   # Exist the loop now
#     print(i)
    
# for i in range(100):
#     if(i == 34):
#         continue  # Skip this iteration
#     print(i)
    

# for i in range(100):
#     pass  # Null statement
# i = 0
# while(i<10):
#     print(i)
#     i +=1
    
    
#Practice set
# n = int(input("Enter a number: "))
# for i in range(1,11):
#     print(f"{n} X {i} = {n*i}")
    
# i = 1
# while(i<11):
#     print(f"{n} X {i} = {n*i}")
#     i+=1


# l = ["Niranjan", "Sohan", "Sachin", "Rahul"]

# for name in l:
#     if(name.startswith("S")):
#         print(f"Hello! {name}")
        
        
# n = int(input("Enter a number: "))
# for i in range(2,n):
#     if(n%i)==0:
#         print("Number is not prime")
#         break
#     else:
#         print("Number is prime")
 

# n = int(input("Enter the number: "))
# i = 1
# sum = 0
# while(i<n):
#     sum += i
#     i += 1
# print(sum)


# n = int(input("Enter the number: "))
# product = 1
# for i in range(1, n+1):
#     product = product * i
    
# print(f"The factorial of {n} is {product}")


# Pattern printing
# n = int(input("Enter the number: "))
# for i in range(1, n+1):
#     print(" "* (n-i), end="")
#     print("*"* (2*i-1), end="")
#     print("") 


# end=""  - use for new line

# n = int(input("Enter the number: "))
# for i in range(1, n+1):
#     print("*"* i, end="")
#     print("")
    

# for i in range(1, n+1):
#     if(i==1 or i==n):
#         print("*"*n, end="")
#     else:
#         print("*", end="")
#         print(" "*(n-2), end="")
#         print("*", end="")
#     print(" ")
    

n = int(input("Enter the number: "))
for i in range(1, 11):
    print(f"{n} X {11-i} = {n*(11-i)}")
    
