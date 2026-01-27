#if condition
#Let us consider the movie "Avenger". This is a 13+ movie.

# print('please enter your date of birth')
# birth_year = int(input())
# current_year = 2025
# age = current_year - birth_year
# if(age<13):
#     print('your are under age, you can\'t watch this movie.') 
#     print('wait until you are old enough to watch this movie')
# else:
#     print('you are old enough to watch Avengers, enjoy!')
#     print('Don\'t forget to watch the sequels and prequels
    
    
# a = int(input('Enter a number: '))
# if(a%2==0):
#     print(a, 'is even number.')
# else:
#     print(a, 'is odd number.')


#x = int(input("Enter a number: "))
# if(x%5==0):
#     if(x%10==0):
#         print('0')
#     else:
#         print('5')
# else:
#     print('other')


# marks = int(input("Enter marks: "))
# if(marks>=0 and marks<=100):
#    if(marks>=90):
#     print('A')
#    if(marks>=80 and marks<90):
#     print('B')
#    if(marks>=70 and marks<80):
#     print('C')
#    if(marks>=60 and marks<70):
#     print('D')
#    if(marks<60):
#     print('E')
# else:
#  print('Invalid input')

 
print('Travel from city A to city B')
Time = int(input('Enter time: '))
Longer = int(input('Define longer: '))
if(Time>=Longer):
    Price = int(input('Enter price: '))
    Higher = int(input('Define higher'))
    if(Price>=Higher):
        print('Train')
    else:
        print('Coach')
else:
    Price = int(input('Enter price: '))
    Higher = int(input('Define higher'))
    if(Price>=Higher):
        print('Daytime flight')
    else:
        print('Red Eye flight')
print('Arrive city B')