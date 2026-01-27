a = (1,34,65.54,"niranjan",False,34,"hello",56)
print(type(a))

b = a.count(34)
print(b)

c = a.index(56)
print(c)

fruits = []
f1 = input("Enter fruit name: ")
fruits.append(f1)
f2 = input("Enter fruit name: ")
fruits.append(f2)
f3 = input("Enter fruit name: ")
fruits.append(f3)
f4 = input("Enter fruit name: ")
fruits.append(f4)
f5 = input("Enter fruit name: ")
fruits.append(f5)
f6 = input("Enter fruit name: ")
fruits.append(f6)
f7 = input("Enter fruit name: ")
fruits.append(f7)
print(fruits)


marks = []
f1 = int(input("Enter marks here: "))
marks.append(f1)
f2 = int(input("Enter marks here: "))
marks.append(f2)
f3 = int(input("Enter marks here: "))
marks.append(f3)
f4 = int(input("Enter marks here: "))
marks.append(f4)
f5 = int(input("Enter fruit here: "))
marks.append(f5)
f6 = int(input("Enter marks here: "))
marks.append(f6)
f7 = int(input("Enter marks here: "))
marks.append(f7)
marks.sort()
print(marks)


l = [3,4,6,7,8]
print(sum(l))