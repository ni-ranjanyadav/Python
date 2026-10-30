# # Opening the file for reading
# file = open("IITM2/example.txt", "r")
# # Writing the file line by line
# for line in file:
#     print(line)
# # Close file
# file.close()



# # Opening the file for writing
# file = open("IITM2/example.txt", "w")
# file.write("Hello, How are you?, My name is Niranjan.\n I'm studying python right now.")
# file.close()



# file = open("IITM2/example.csv", 'w')
# file.writelines("Name, RollNo, PhoneNumber, Email\n")
# file.writelines("studentid, class, score, subject")
# file.close()

# file = open("IITM2/example.csv", 'r')
# for line in file:
#     print(line)
# file.close()



# file = open("IITM2/example.txt", 'r')
# l = file.readlines()
# print(l)

# print(l[0])
# print(l[1])
# file.close()


# file = open("IITM2/example.txt", 'r')
# first_line = file.readline()
# print(first_line.strip())
# second_line = file.readline()
# print(second_line.strip())
# third_line = file.readline()
# print(third_line.strip())
# fourth_line = file.readline()
# print(fourth_line.strip())
# file.close()


# file = open("IITM2/example.csv", 'r')
# print(file.read())
# file.close()


# f = open("IITM2/example.txt", 'r')
# print(f.tell())  # tell() tells you the current position of the file pointer.
# f.close()


# f = open("IITM2/example.txt", 'r')
# print(f.read(15))
# print(f.tell())
# f.close()


# f = open("IITM2/example.txt", 'r')
# f.seek(16)  # seek(position) moves the pointer to a specified position.
# print(f.read())
# f.close()


# file = open("IITM2/example.txt", 'a')
# file.writelines("\nI currently live in a hostel 4")
# file.close()


# file = open("IITM2/example.txt", 'a+')
# file.writelines("\nI'm studying in a 5th sem")
# file.seek(0)
# print(file.read())
# file.close()


# def read_file(filename, n):
#     with open(filename, "r") as f:
#         lines = f.readlines()
#         if n<=len(lines):
#             return lines[n-1].rstrip("\n")
#         else:
#             return None

# print(read_file("IITM2/public1.txt", 2))



# def do_something(filename, sub):
#     f = open(filename, 'r')
#     # Ignore the header
#     f.readline()
#     # we are now at the beginning of the second line of the file
#     val, count = 0, 0
#     for line in f:
#         sno, name, gender, ct, python, pdsa = line.strip().split(',')
#         sno, ct, python, pdsa = int(sno), int(ct), int(python), int(pdsa)
#         if sub == 'CT':
#             val = val + ct
#         elif sub == 'Python':
#             val = val + python
#         elif sub == 'PDSA':
#             val = val + pdsa
#         count = count + 1
#     f.close()
#     return val / count
# # Hint: int(1.5) is 1
# print(int(do_something('IITM2/score.csv', 'Python')))


# def get_scores(filename, index):
#     f = open(filename, 'r')
#     # Ignore the header
#     f.readline()
#     # We are now at the beginning of the second line of the file
#     scores = []
#     line = f.readline()
#     while line != '':
#         L = line.strip().split(',')
#         scores.append(int(L[index]))
#         line = f.readline()
#     f.close()
#     return scores
# print(get_scores("IITM2/score.csv", 3))



# def get_scores(filename, index):
#     f = open(filename, 'r')
#     # Ignore the header
#     f.readline()
#     scores = []
#     line = f.readline()
#     while line != '':
#         L = line.strip().split(',')
#         scores.append(int(L[index]))
#         line = f.readline()
#     f.close()
#     return scores
# def do_something(L):
#     L.sort()
#     mid = len(L) // 2
#     if len(L) % 2 == 0:
#         return (L[mid] + L[mid - 1]) // 2
#     else:
#         return L[mid]

# print(do_something(get_scores('IITM2/score.csv', 4)))


# def do_something(infile, gender, outfile):
#     f = open(infile, 'r')
#     g = open(outfile, 'w')
#     header = f.readline()
#     # We are now at the beginning of the second line of the file
#     # 'good,M,great'.replace(',M,', ',')
#     # returns 'good,great'
#     header = header.replace(',Gender,', ',')
#     g.write(header)
#     for line in f.readlines():
#         fields = line.strip().split(',')
#         gender_in_file = fields[2]
#         if gender_in_file == gender:
#             out_line = line.replace(f',{gender},', ',')
#             g.write(out_line)
#     f.close()
#     g.close()

# do_something('IITM2/score.csv', 'F', 'IITM2/out.csv')


# def do_something(filename):
#     f = open(filename, 'r')
#     maxword = f.readline().strip()
#     count = 1
#     # We are now at the beginning of the second line
#     for line in f:
#         word = line.strip()
#         if len(word) > len(maxword):
#             maxword = word
#             count = 1
#         elif len(word) == len(maxword):
#             count += 1
#     f.close()
#     return count

# print(do_something('IITM2/word.txt'))


# def get_freq(filename):
#     f = open(filename, 'r')
#     d = {}
#     line = f.readline().strip()
#     while line != "":
#         if line in d:
#             d[line] += 1
#         else:
#             d[line] = 1
#         line  = f.readline().strip()
#     f.close()
#     return d
# print(get_freq("IITM2/public_1.txt"))


# def relation(file1, file2):
#     f1 = open(file1, 'r')
#     f2 = open(file2, 'r')
    
#     line1 = f1.readline().strip()
#     line2 = f2.readline().strip()
#     while line1 != "":
#         if line1 != line2:
#             return "No Relation"
        
#         line1 = f1.readline().strip()
#         line2 = f2.readline().strip()

#     if line1 == line2:
#         return "Equal"
#     else:
#         return "Subset"
    
#     f1.close()
#     f2.close()
# print(relation("IITM2/text1", "IITM2/text2"))


# def get_goals(filename, country_name):
#     f = open(filename, 'r')
#     num_player = 0
#     num_goals = 0
#     line = f.readline().strip()
#     while line != "":
#         fields = line.split(",")
#         if fields[1] == country_name:
#             num_player += 1
#             num_goals += int(fields[2])
#         line  = f.readline().strip()
#     f.close()
#     if num_player == 0:
#         return (-1, -1)
#     return (num_player, num_goals)
# print(get_goals("IITM2/public_1.csv", "Brazil"))


f = open("hello.txt", "w")
f.write("Hello World how are you today")
f.close()    

f = open("hello.txt", "r")
data = f.readlines()
for line in data:
    words = line.split()
    print(words)
f.close()
