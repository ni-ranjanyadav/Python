# a = 5
# b = 7
# print(a+b)
# print("Niranjan yadav")
#print("'Hello, I am learning python.'")

# price = 80
# discount_percent = 2
# discounted_price = price - (price * discount_percent/100)
# print(round(discounted_price))

# total_mins = 270
# mins = total_mins%60
# hrs = total_mins//60
# print(mins)
# print(hrs)

# a = 4
# if (a>=5):
#     print(True)
# else:
#     print(False)

# # One line if else statement in python
# result = True if a>=5 else False
# print(result)

# a = -11
# if(a%2!=0 or a<10):
#     print(True)
# else:
#     print(False)

# result = True if a%2!=0 and a in range(-10,10) else False
# print(result)

# price1, discount1, price2, discount2 = 150, 25, 200, 45
# offer1 = price1 * (100 - discount1) / 100
# offer2 = price2 * (100 - discount2) / 100
# print(offer1,offer2)
# is_offer1_cheaper = offer1 < offer2
# result = True if is_offer1_cheaper else False
# print(result)


# s = "hello python"
# course_code = "24t2cs100"
# result1 = s[2] # third char of str
# result2 = s[-4] # fourth last char of str
# result3 = s[0:3] # first 3 char of str
# result4 = s[::2] # every second char of str
# result5 = s[-3:] # last 3 char of str
# result6 = s[::-1] # reverse the string

# print(result1)
# print(result2)
# print(result3)
# print(result4)
# print(result5)
# print(result6)
# course_term = course_code[3]
# course_year = course_code[0:2]
# print(course_term)
# print(course_year)


# word1 = "wingardium"
# word2 = "Leviyosa"
# word3 = "Silver"
# sentence = "Learning python is fun"
# n1 = 6
# n2 = 4
# print(word2+" "+word3)
# print(word2[:4] + "-" + word3[-4:])
# print(word2 + " " + str(n1))
# print("-" *n2)
# print(str(n1)*n2)
# print(True if word1==word2==word3 else False)
# print(True if word1<word2 and word1<word3 else False)
# print(True if 'h' in word1 else False)
# print(True if word1.endswith('a' or 'A') else False)
# print(True if 'python' in sentence else False)

# num = 9
# print(f"{num:02d}") # 02d means - 'd' display as an integer, '2' use at least two digit, '0' fill empty space with zero

# dob = input("enter your dob: ")
# day, month, year = int(dob.split('/')[0]), int(dob.split('/')[1]), int(dob.split('/')[2])
# print(f"{day:02d}/{month:02d}/{year + 5}")

'''Highest
()
**    exponent operator ** is right-associative in Python if multiple ** in single line
*, /, //, %    have the same precedence (these operators are evaluated from left to right.)
+, -    have the same precedence (these operators are evaluated from left to right.)
Lowest'''

# print("a+'b'+c+''+d")
# print(1234)
# print("1 2 3 4")
# print(1, 2, 3, 4) # Comma give the space b/w the number
# print(1)
# print(2)
# print(3)
# print(4)
# print('a','b') # Comma give a space b/w the words or number also
# print('a b')

# print(15%3*3+2)
# print(type(13 % 5 // 2 * 30 ** 5)) # // return int value
# print(type(20 ** 10 / 2 + 25 - 70)) # / always return float value in python
# word = 'niranjan'
# new_word = word[0]+word[len(word)-1]
# print(new_word)
# w1 = input()
# w2 = input()
# print(w1+w2)
# print(type(2**3**0)) # exponents is evaluated from right to left
# print(type(5**2.0))
# print(type(5==2))
# print(type(5 and 2 or '3'))

# 'AND', 'OR' operator in python
'''Python evaluates 'and' from left to right.
Return the first falsy value.
If there is no falsy value, return the last value.
5 and 2 and 8      # 8
5 and 0 and 8      # 0
0 and 5 and 8      # 0

Python evaluates 'or' from left to right.
Return the first truthy value.
If there is no truthy value, return the last value.
0 or 2 or 8        # 2
0 or "" or 8       # 8
5 or 2 or 8        # 5

Zero(0) means false in python.
One(1) means true in python.'''

# print(type(5==5 and '4'))
# print(type("555""[2]"))
# print(type('False'))

# print(int("5.0")+float(2)) # Here string not directly converted into int because it depends on inside value
# print(float("5.0")+float(2)) # Here string first converted into float because inside value is float
# print(int(float("5.0"))+float(2))

'''Whenever Python sees chained comparisons:
a < b < c
a == b > c
a <= b != c
it always interprets them as:
(a < b) and (b < c)
(a == b) and (b > c)
(a <= b) and (b != c)'''

# print(5==5>3)
# print((5==5)>3)
# print(5==(5>3))
# print(5==5 and 5>3)
# print(5==5 or 5>3)
# print(3==3>2==2)
# print((3==3)>(2==2))
# print(3==(3>2) and (3>2)==2)

'''The precedence is:
not - highest
and
or - lowest'''

# print(3 and not 4 or not 5) # This can be also written as (3 and (not 4) or (not 5))
# print(3 and (not (4 or not 5)))
# word = '138412345678901938'
# print(word[4:13])

# expr_1 = True
# expr_2 = False
# expr_3 = not (expr_1 or expr_2)
# expr_4 = (not expr_1) and (not expr_2) 
# print(expr_3 == expr_4)
# n = 2
# print(n<=4)


items = ["pen", "pencil", "erasser", "marker"]
out = []
for i in range(len(items)):
    for j in range(i):
        if len(items[i]) != len(items[j]):
            out.append(items[i])
            break
print(out)