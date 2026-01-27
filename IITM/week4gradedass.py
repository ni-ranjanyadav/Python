# import random  # Function to generate random number

# rolls = []   # Here we create a empty list variable to store dice roll
# for i in range(100000):    # i is a iterator to start the loop from i=0 to i=n-1 
#     #randint include the endpoint
#     roll = random.randint(1,6)  # Here we create a variable roll to store  single dice throw which is not in list form just generate 10000 random number between 1 to 6 
#     rolls.append(roll)    # This line used to add an element in variable rolls in list form
#     print(roll)
# print(rolls)
# # We are intrested in finding total prime number from 100000 times dice throw prime no. are 2,3,5 how many 2,3,5 are there
# count = 0 # So, we initilize 
# primes = [2,3,5]
# for roll in rolls:  # Take each value from the list rolls one by one temporarily call it roll inside the loop [[purpose of the for-loop is to go through every dice roll stored in the list rolls
#     if roll in primes:  # Check if any prime apper in roll 
#         count += 1    # If condition is true it count 

# print(sys.getsizeof(rolls))
# print(len(rolls))
# some_var = count/len(rolls) # It give the probability that a number choosen from the list is prime
# print(some_var)
# print(count)


# L = [5,6,7,8,9,10,11,12,13,14]
# S = 0    # We inisitilize sum = 0 it will store sum of all element in L
# for x in L:   # x can take every element of L one by one
#     #print(x)   
#     S += x    # sum = sum + x ; x is a element of list L
# # print(S)
# # print(len(L))
# flag = False   # we assume above condition is false
# y = -1     # now we create a another variable y which store the value -1
# for x in L:      # x can take every element of l one by one (again)
#     if x * len(L) == S:   # check if x * len(l) i.e. x * 10 is equals to S 
#         flag = True   # if condition is true, set flag true
#         y = x     # if above condition is true then that value of x store in y
#         break      #  Exist from the loop once condition is met
#     # print(x)
#     # print(y)

# # CODE TO PRINT THE LIST IN ASCENDING ORDER
# L = [90, 47, 8, 18, 10, 7]
# #print(len(L))
# S = [L[0]]	# list containing just one element, i.e S = [90]
# for i in range(1, len(L)):     # i = 1, 2, 3, 4, 5  ; len(L) = 6
#     #print(i)
#     flag = True    #  Assume we'll add L[i] at the end unless condition change
#     for j in range(len(S)):     # Compare L[i] with each element in S
#         if L[i] < S[j]:         # Found a possition where L[i] is smaller than S[j]
#             before_j = S[: j]	# elements in S before index j
#             new_j = [L[i]]		# list containing just one element
#             after_j = S[j: ]	# elements in S starting from index j
#             # what is the size of S now?
#             # before updating size of S is len(s)
#             S = before_j + new_j + after_j
#             # what is the size of S now?
#             # after updating size of S is still the same as before+1(since we insert one element)
#             flag = False
#             break      # Stop checking once updated
#     if flag:
#         S.append(L[i])
# print(S)


# points = [ ]
# for x in range(0, 5):
#     for y in range(0, 5):
#         points.append([x, y])
# print(points)
# print(type(points))

# L = [y - x for x in [1, 2, 3] for y in [3, 4, 5] if y > x]
# print(L)
# # This code also written as 
# L = [ ]
# for x in [1, 2, 3]:
#     for y in [3, 4, 5]:
#         if y > x:
#             L.append(y - x)
# print(L)


# L = [ ]
# for y in [3, 4, 5]:
#     for x in [1, 2, 3]:
#         if y > x:
#             L.append (y - x)
# print(L)

# triplets = [ ]
# for x in range(1, 100):
#     for y in range(x + 1, 100):
#         for z in range(y + 1, 100):
#             if x ** 2 + y ** 2 == z ** 2:
#                 triplets.append((x, y, z))
# print(triplets)


# L = ['Niranjan','Simmi','simmi', 'yadav']
# P = [ ]
# for name in L:
#     if 'A' <= name[0] <= 'Z':
#         P.append(name)
# print(name)

# P = [name for name in L if 'A' <= name[0] <= 'Z']
# print(P)

# P = [name for name in L if 'a' <= name[0] <= 'z']
# print(P)


# P = input().split(',')
# L = [ ]
# for word in P:
#     if 'e' not in word:
#         L.append(word)
# print(L)

# L = [word for word in input().split(',') if 'e' not in word]
# print(L)

# print([word for word in input().split(',') if 'e' not in word])


# def minmax(a, b):
#     if a <= b:
#         return a, b
#     return b, a

# def unique(L):
#     L_uniq = [ ]
#     for i in range(0, len(L)):
#         if not(L[i] in L[i+1:]):
#             L_uniq.append(L[i])
#     return L_uniq

# L = [1,1,2,3,5,5]
# print(unique(L))
# L = [1,2,3,4,5,7,7]
# print(unique(L))


# def poly(L, x_0):
#     psum = 0
#     n = len(L)
#     for i in range(n):
#         psum = psum + L[i] * (x_0 ** i)
#     return psum

# print(poly([1,2,3],5))

# def poly_zeros(L, a, b):
#     zeros = [ ]
#     for x in range(a, b + 1):
#         if poly(L, x) == 0:
#             zeros.append(x)
#     return zeros

# print(poly_zeros([2, -3, 1], 0, 4))

# def poly(L, x_0):
#     psum = 0
#     n = len(L)
#     for i in range(n):
#         psum = psum + L[i] * (x_0 ** i)
#     return psum

# def poly_zeros(L, a, b):
#     zeros = []
#     for x in range(a, b + 1):
#         if poly(L, x) == 0:
#             zeros.append(x)
#     return zeros

# # Given polynomial coefficients
# L = [-180, -144, 101, 52, -18, -4, 1]

# print(poly_zeros(L, 0, 4))
