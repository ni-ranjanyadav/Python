#NUMBER
# # Write a function to calculate the percentage increased from the original value to the new value.
# original_value = float(input("Enter original value: "))
# new_value = float(input("Enter new value: "))
# def percentage_increased(original_value, new_value):
#     return(((new_value-original_value)/original_value)*100)

# print(f'percentage increased is:',(percentage_increased(original_value,new_value)))


# # Write a function to check if a number is a ten-digit even number.
# # Also account for negative numbers discarding the sign.
# n = abs(int(input("Enter number: ")))
# def is_ten_digits_even_number(n):
#     return((len(str(n))) == 10 and n % 2 == 0)   # First convert n into string then we find length because str number has no length

# print(is_ten_digits_even_number(n))


# Given a tuple of two integers (a, b), return a tuple containing the sum, difference, 
# product, and quotient (integer division) of the two numbers.
# a = int(input())
# b = int(input())
# def arthmetic_operation(a,b):
#     return(a+b,a-b,a*b,a//b)

# print(arthmetic_operation(a,b))


#STRING
#Given a tuple of length two create a string in the format of "second, first" 
# where first and second are the first and second elements in the tuple.



# # OPPE PRACTICE
# a = int(input("a = "))
# b = int(input("b = "))
# def sum_square_abs_diff_squares(a,b):
#     return((a**2 + b**2), abs(a**2 - b**2))

# print(sum_square_abs_diff_squares(a,b))


a = int(input("a = "))
def describe_number(a):
    if(a%5==0 and a%3==0):
        print("'FizzBuzz'")
    elif(a%5==0):
        print("'Buzz'")
    elif(a%3==0):
        print("'Fizz'")
    else:
        print("'normal'")
    
(describe_number(a))