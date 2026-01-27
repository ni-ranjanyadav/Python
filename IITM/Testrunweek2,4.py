
# # Read the operation name
# operation = input().strip()

# # Odd number checker
# if operation == "odd_num_check":
#     number = int(input())
#     if number % 2 != 0:
#         print("yes")
#     else:
#         print("no")
        
# # Prefect square check
# elif operation == "perfect_square_check":
#     number = int(input())
#     if int(number**0.5)**2 == number:
#         print("yes")
#     else:
#         print("no")

# # Vowel check
# elif operation == "vowel_check":
#     text = input().strip()
#     vowels = 'aeiouAEIOU'
#     if any(char in vowels for char in text):
#         print("yes")
#     else:
#         print("no")
        
# # Divisibility checker
# elif operation == "divisibility_check":
#     number = int(input())
#     if number%6 == 0:
#         print("divisible by both 2 and 3")
#     elif number%2 == 0:
#         print("divisible by 2")
#     elif number%3 == 0:
#         print("divisible by 3")
#     else:
#         print("not divisible by 2 and 3")
        
# # Palindrominator
# elif operation == "palindrominator":
#     text = input().strip()
#     result = text + text[-2::-1]  # text[-2:-1] - it means start from second last char and goes backward till beginning.
#     if len(text) > 1:
#         print(result)
#     else:
#         print(text)
    
# #Simple interest calculator
# elif operation == "simple_interest":
#     principal_amount = int(input())
#     n_year = int(input())
#     rate = 0.05 if n_year < 10 else 0.08
#     si = principal_amount * rate * n_year
#     print(round(si))


# import math
# x = int(input())
# p = math.sqrt(x)
# r = p**2      # p^2
# print(x)
# print(p)
# print(r)
x = 1//10
print(x)