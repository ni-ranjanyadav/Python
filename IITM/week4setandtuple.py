#SET
# A = {1,2,3,4,5}
# B = {1,6,5,9}
# print(A.issubset(B))
# print(B.issubset(A))

# print(A.issuperset(B))
# print(B.issubset(A))

# print(A.union(B))
# print(A|B)   # This symbol is also used for union

# print(A.intersection(B))
# print(A&B)

# print(A.difference(B))
# print(A - B)


# TUPLE
# t = 1,2,3
# print(t,(type(t)))
# x,y,z = t
# print(x,y,z)

# l = [10]
# print(l, type(l))

t = (10,)
print(t,type(t))

# t = ([1, 2], ['a', 'b'])
# # t[0] = [10, 20]  # This is wrong
# print(t)
# t[0][0] = 10  # This is right
# print(t)



#LIST COMPREHENSION
# a = 10
# b = 20
# '''if a<b:
#     small = a
# else:
#     small = b'''
# # This if-else block of code is written in one line
# small = a if a<b else b
# print(small)

fruits = ['mango', 'apple', 'banana', 'orange', 'pineapple', 'watermellon', 'guava', 'kiwi']
# newlist = []
# for fruit in fruits:  # In place of fruit we create any variable just to store(e.g. i,n,anyname etc)
#     if 'p' in fruit:
#         newlist.append(fruit.capitalize())
# print(newlist)

newlist = [fruit.capitalize() for fruit in fruits if 'n' in fruit]
print(newlist)