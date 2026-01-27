# f = open('mytext.txt','w')
# f.write('Niranjan Yadav')
# f.write('\n')
# f.write('Python')
# f.close()

# x = open('mytext.txt','r')
# s = x.read()
# print(s)


# import string

# def create_caesar_dictionary():
#     l = string.ascii_lowercase
#     l = list(l)
#     d = {}
#     for i in range(len(l)):
#         d[l[i]] = l[(i+3)%26]
#     return d

# f = open('sherlock.txt','r')
# g = open('encrypted_sherlock.txt','w')
# d = create_caesar_dictionary()

# c = f.read(1)
# while(c!=''):
#     g.write(d[c])
#     c = f.read(1)
    
# f.close()
# g.close()

# f = open('test.txt','r')
# s = f.read(2)
# print(s)
# s = f.read(2)
# print(s)

# p = f.seek(4)
# print(p)
# s = f.read(1)
# print(1)
# q = f.seek(7)
# print(q)

# RECURSION

# n = 10
# ans = 0
# for i in range(n):
#     ans = ans+(i+1) 
# print(ans)


# def sum(n):
#     if (n==1):
#         return 1
#     else:
#         return n + sum(n-1)


# def comp(p,n):
#     if(n==1):
#         return p*(1.1)
#     else:
#         return(comp(p,n-1))*1.1

# print(comp(2000,3))


# def check0(l):
#     if (len(l) == 0):
#         return 0
#     if(l[0] == 0):
#         return 1
#     else:
#         return check0(l[1:len(l)])
    
# ans = (check0([1,2,3,4,5,10,8,7,3]))
# print(ans)


# #SHORTING
# def mini(L):
#     mini = L[0]
#     for x in L:
#         if(x < mini):
#             mini = x
#     return mini

# def sort(L):
#     if(L == []) or (len(L)==1):
#         return L
#     m = mini(L)
#     L.remove(m)
#     return [m] + sort(L)

# L = [5,6,8,5,4,5]
# print(sort(L))


#GRADED ASSIGNMENT - 8

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
# print(int(do_something('scores.csv', 'Python')))



# def get_scores(filename, index):
#     f = open(filename, 'r')
#     # Ignore the header
#     f.readline()	
#     # we are now at the beginning of the second line of the file
    
#     scores = [ ]
#     line = f.readline()
#     while line != '':
#         L = line.strip().split(',')
#         scores.append(int(L[index]))
#         line = f.readline()
    
#     f.close()
#     return scores
# print(get_scores('scores.csv', 3))

# def do_something(L):
#     L.sort()
#     mid = len(L) // 2
#     if len(L) % 2 == 0:
#         return (L[mid] + L[mid - 1]) // 2
#     else:
#         return L[mid]
    
# print(do_something(get_scores('scores.csv', 4)))



# def do_something(filename):
#     f = open(filename, 'r')
#     maxword = f.readline().strip()
#     count = 1
#     # we are now at the beginning of the second line
#     for line in f:
#         word = line.strip()
#         if len(word) > len(maxword):
#             maxword = word
#             count = 1
#         elif len(word) == len(maxword):
#             count += 1
    
#     f.close()
#     return count

# print(do_something('words.txt'))


# def get_freq(filename):
#     """
#     Extract frequency information from the file

#     Argument:
#         filename: string, path to file
#     Return:
#         result: dictionary; keys are strings, values are integers
#     """
#     f = open(filename,'r')
#     result = {}
#     for line in f:
#         words = line.strip().split()
#         for w in words:
#             if w in result:
#                 result[w] += 1
#             else:
#                 result[w] =1
#     f.close()
#     return result
        
# print(get_freq('public_1.txt'))



def relation(file1, file2):
    f1 = open(file1, 'r')
    f2 = open(file2, 'r')
    line1 = [line.strip() for line in f1.readlines()]
    line2 = [line.strip() for line in f2.readlines()]
    
    f1.close()
    f2.close()
    
    f1_len = len(line1)
    f2_len = len(line2)
    
    same_prefix = True
    for i in range(f1_len):
        if line1[i] != line2[i]:
            same_prefix = False
            break
    
    if same_prefix:
        if f1_len == f2_len:
            return 'Equal'
        elif f1_len < f2_len:
            return 'Subset'
    return 'No Relation'

print(relation('public_1_1.txt', 'public_1_2.txt'))
