# try:
#     a = int(input("Enter a number:"))
#     print(a)
    
# except Exception as e:
#     print("Please enter a valid number")



# # Raise Exception
# a = int(input("Enter a first number: "))
# b = int(input("Enter a second number: "))

# if(b == 0):
#     raise ZeroDivisionError("Hey our program is not meant to divide number by zero")
# else:
#     print(f"The division a/b is {a/b}")



# def main():
#     try:
#         a = int(input("Hey, Enter a Number:"))
#         print(a)
#         return 

#     except Exception as e:
#         print(e)
#         return
        
#     finally:
#         print("Hey, I am inside of finally.")
   
# main()



# def myFunc():
#     print("Hello World!")
    
# myFunc()
# print(__name__)



# def myFunc():
#     print("Hello World!")

# if __name__ == "__main__":
#     print("We are directly running this code.")
#     myFunc()
#     print(__name__) 
    
    

# # Enumerate Function
# l = [3, 513, 56, 876]

# for index, item in enumerate(l):
#     print(f"The item number at index {index} is {item}")
    
    
    
# my_list = [1, 3, 6, 3, 5, 9]

# squard_list = []
# for item in my_list:
#     squard_list.append(item*item)
    
# print(squard_list)



# try:
#     with open("1.txt", "r") as f:
#         print(f.read())
# except Exception as e:
#     print(e)

# try:        
#     with open("2.txt", "r") as f:
#         print(f.read())
# except Exception as e:
#     print(e)
  
# try:        
#     with open("3.txt", "r") as f:
#         print(f.read())
# except Exception as e:
#     print(e)


# l = [1,2,3,4,5,6,7]
# for i, item in enumerate(l):
#     if i == 2 or i == 4 or i == 6:
#         print(item)



# n = int(input("Enter a number: "))
# table = [n*i for i in range(1, 11)]
# print(table)


n = int(input("Enter a number: "))
table = [n*i for i in range(1, 11)]
with open("table.txt", "a") as f:
    f.write(f"Table of {n}: {str(table)}\n")
    
