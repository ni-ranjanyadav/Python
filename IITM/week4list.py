# LIST - []
# SET - {}
# TUPLE - ()


# l = [1, 7, 5, 3, 2]
# print(l)

# l.append(50)
# print(l)

# l.remove(1)
# print(l)

# l.append(2)
# print(l) 

# l.remove(2)
# print(l)

# x = []
# x.append(l)
# print(x)
# x.append(m)
# print(x)
# m = [10, 20, 30]
# m = []
# m.append([1, 2, 3])
# m.append([2, 3, 4])
# m.append([4, 5, 6])
# print(m)


# l = [10]
# l = [1,2,3,4,5,6,7,8,9,0]
# print(l[6])
# l.append('niranjan')
# print(l)
# x = 5 in l
# print(x)


# l = list(range(1000000000))
# print(l[19999])
# print(l[0])


# x = [1,2,3,4,5,6]
# print(x)
# print(type(x))
# y = {1,2,3,3,4,5,5,6}
# print(y)
# print(type(y))
# z = (1,2,3,4,5,6,8)
# print(z)
# print(type(z))


# import sys
# l = []
# l1 = [0]
# l2 = [0,1]
# print(sys.getsizeof(l))
# print(sys.getsizeof(l1))
# print(sys.getsizeof(l2))

# x = list(range(100))
# s = set(range(100))
# print(x)
# print(sys.getsizeof(x))
# print(s)
# print(sys.getsizeof(s))


# z = {'niranjan', 'kartik', 'suruchi', 'aryan'}
# z.add('kriti')
# print(z)
# p = 'aryan' in z
# print(p)
# q = 'neeraj' in z
# print(q)


# #Tuple
# t = (1,2,3,4,5,6)
# print(type(t))
# # A tuple is unchangable and list, set is changable


# import string
# s1 = string.ascii_letters
# print(s1)
# s2 = string.ascii_lowercase
# print(s2)
# print(set(s2))
# print(tuple(s2))
# print(list(s2))

# s = 'niranjan$$%^^&*$# yadavINDIA676#@$%'
# l = list(s)
# s1 = string.ascii_letters
# r = []
# for p in s:      # I will take a variable p for storing alphabet store in s
#     if p in s1:
#         r.append(p)
# print(r)


# import sys
# t = tuple(range(10))
# print(t)
# print(type(t))
# print(sys.getsizeof(t))


# l1 = [1,2,3]
# l2 = [20,30,40]
# l12 = l1 + l2
# l21 = l2 + l1
# print(l12,l21)

# l1 = [0] * 10
# print(l1)
# l2 = [1,2,3] * 5 
# print(l2)
# print(l1 == l2)

# l = [1,2,3]
# print(l)
# l[2] = 4
# print(l)

# print([1,2] > [2,1])
# # 1>2 - no then false does not check 2nd element
# print([3,4] > [2,3])
# # 3>2 - yes, then check - 4>3 yes then print True


# x = 5 
# y = x 
# x = 10
# print(x,y)
# l1 = [1,2,3]
# l2 = l1
# l1[0] = 100
# print(l1,l2)


# l1 = [1,2,3]
# l2 = list(l1)
# l3 = l1[:]
# l4=l1.copy()
# l5 = l1
# print(l1 is l2)
# print(l1 is l3)
# print(l1 is l4)
# print(l1 is l5) 


# def add(x):
#     x.append(1)
#     return x
# x = [5]
# print(add(x))
# print(x)


# l = [1,2,3]
# print(l)

# l.append(4)
# print(4)
# print(l)

# l.remove(2)
# print(l)

# x = l.copy()
# print(x,1)

# l.insert(0,9)   # First digit tell about where you want to insert
# print(l)
 
# l.pop(0)  # Pop used for deleating the ith element
# print(l)

# Sorting 
# l = [72,6,8,45,1,5,95,23,12,89,5,3,4,0]
# l.sort()
# print(l)

# l.reverse()
# print(l)