class Student:
    def __init__(self, roll_no = None, name = None) -> None:
        self.roll_no = roll_no
        self.name = name

s0 = Student()
s0.roll_no = 0
s0.name = 'niranjan'
print(s0.roll_no, s0.name)

s1 = Student()
s1.roll_no = 1
s1.name = 'aryan'
print(s1.roll_no, s1.name)

s2 = Student()
s2.roll_no = 2
s2.name = 'kartik'
print(s2.roll_no, s2.name)

s50 = Student()
s50.name = 'suruchi'
print(s50.roll_no, s50.name)



# class Student:
#     count = 0
#     def __init__(self, roll_no, name, total):
#         self.roll_no = roll_no
#         self.name = name
#         self.total = total
    
#     def display(self):
#         print(self.roll_no, self.name, self.total)
        
#     def result(self):
#         if self.total > 120:
#             print('pass')
#         else:
#             print('fail')
        
# s0 = Student(0, 'Niranjan', 130)
# Student.count += 1
# s0.display()
# s0.result()

# s1 = Student(1, 'kartik', 110)
# Student.count += 1
# s1.display()
# s1.result()
# print(Student.count)



# class Person:       # This is parent class
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print(self.name, self.age)

# class Student(Person):          # This is sub class of parent class
#     def __inti__(self, name, age, marks):
#         super().__init__(name,age)
#         self.marks = marks

#     def display(self):
#         super().display()
#         print(self.marks)

# class Employee(Person):          # This is also sub class of parent class
#     def __inti__(self, name, age, salary):
#         super().__init__(name,age)
#         self.salary = salary
        
#     def display(self):
#         super().__init__(name,age)
#         print(self.salary)

# s = Student('ride', 20, 250)
# s.display()
# e = Employee('Harsh', 30, 50000)
# e.display()



# class Student:
#     count = 0
#     def __init__(self, name, roll, maths, physics, chemistry):
#         Student.count += 1
#         self.roll = roll
#         self.name = name
#         self.maths = maths
#         self.physics = physics
#         self.chemistry = chemistry

# class Group:
#     def __init__(self):
#         self.members = [ ]

#     def add(self, student):
#         self.members.append(student)

#     def print_members(self):
#         for student in self.members:
#             print(student.name)
            
            

D = {'Anita': 23, 'Ashwin': 43,
     'Ahana': '24',
     'Adarsh': 30, 'Archana': 15}
try:
    # iterates through the keys from left to right
    for key in D:
        value = D[key]
        if type(value) == str:
            raise ValueError ("Error")
        print(f'{key}:{value}')
except:
    print("Values cannot be strings")
    
    

L = [1, 3, -1, 4, -2, 5, 3]

try:
    n = 10
    for i in range(len(L)):
        if L[i] < 0:
            L[i] = 0

    for i in range(n - len(L)):
        L.append(0)
except IndexError:
    pass
finally:
    print(L)
    
    

try:
    L = [x for x in range(10)]
    f = open('numbers.txt', 'w')
    for x in L:
        f.write(str(x))
except FileNotFoundError:
    print('File was not found')
except:
    print('This is some other error')
finally:
    print('The file has been closed')

    
    
class calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def substract(self):
        return self.a - self.b
    def quotient(self):
        return self.a // self.b
    def remainder(self):
        return self.a % self.b
        
        
        
class StringManipulation:
    def __init__(self, words):
        self.words = words

    def total_words(self):
        return len(self.words)

    def count(self, some_word):
        return self.words.count(some_word)

    def words_of_length(self, length):
        return [w for w in self.words if len(w) == length]

    def words_start_with(self, char):
        return [w for w in self.words if w.startswith(char)]

    def longest_word(self):
        return max(self.words, key=len)

    def palindromes(self):
        return [w for w in self.words if w == w[::-1]]



class Shape:
    def __init__(self, side):
        self.side = side

        self.compute_area()
        self.compute_perimeter()

    def compute_area(self):
        self.area = self.side * self.side

    def compute_perimeter(self):
        self.perimeter = 4 * self.side
        

class Time:
    def __init__(self, time):
        self.time = time

    def seconds_to_minutes(self):
        minutes = self.time // 60
        seconds = self.time % 60
        return f"{minutes} min {seconds} sec"

    def seconds_to_hours(self):
        hours = self.time // 3600
        remaining = self.time % 3600
        minutes = remaining // 60
        seconds = remaining % 60
        return f"{hours} hrs {minutes} min {seconds} sec"

    def seconds_to_days(self):
        days = self.time // 86400
        remaining = self.time % 86400
        hours = remaining // 3600
        remaining = remaining % 3600
        minutes = remaining // 60
        seconds = remaining % 60
        return f"{days} days {hours} hrs {minutes} min {seconds} sec"
