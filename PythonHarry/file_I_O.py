# f = open("words.txt")
# data = f.read()
# print(data)
# f.close()


st = "Hey! I am Niranjan Yadav."
# f = open("mytext.txt","w")
# f.write(st)
# print(st)
# f.close()


# f = open("file.txt")
# lines = f.readlines()
# print(lines, type(lines))
# f.close()


# # Append the file
# f = open("mytext.txt","a")
# f.write(st)
# f.close()


# f = open("file.txt")
# print(f.read())
# f.close()

# The same things can be written using "with statement" like this.

# with open("file.txt") as f:
#     content = f.read()
#     if("twinkle" in content):
#         print("The word twinkle is present in this content.")
    
#     else:
#         print("The word twinkle is not present in this content.")
        
        
# Game Function


# import random

# def game():
#     print("You are playing the game.")
#     score = random.randint(1, 62)
    
#     with open("hi_score.txt") as f:
#         hi_score = f.read()
        
#         if(hi_score == ""):
#             hi_score = 0
#         else:
#             hi_score = int(hi_score)
        
#     print(f"your score: {score}")
    
#     if(score > hi_score):
#         with open("hi_score.txt", "w") as f:
#             f.write(str(score))
#         print("New High Score!")
#         hi_score = score
        
#     return hi_score
    
# game()



# def generateTable(n):
#     table = ""
#     for i in range(1,11):
#         table += f"{n} X {i} = {n*i}\n"
    
#     with open(f"table/table_{n}.txt", "w") as f:
#         f.write(table)
        
# for i in range(1,21):
#     generateTable(i)


# with open("table/test.txt", "w") as f:
#     f.write("Hello")


# word = "Twinkle"

# with open("file.txt" ,"r") as f:
#     content = f.read()
    
# contentNew = content.replace(word, "######")

# with open("file.txt" ,"w") as f:
#     f.write(contentNew)


# words = ["Twinkle", "little"]

# with open("file.txt" ,"r") as f:
#     content = f.read()
    
# for word in words:
#     content = content.replace(word, "#" * len(word))

# with open("file.txt" ,"w") as f:
#     f.write(content)
    
    
    
# with open("log.txt") as f:
#     content = f.read()

# if("python" in content):
#     print("yes python is present.")
# else:
#     print("python is not present.")



# with open("log.txt") as f:
#     lines = f.readlines()
    
# lineno = 1
# for line in lines:
#     if("python" in line):
#         print(f"yes python is present. Line no: {lineno}")
#         break
#     lineno += 1 

# else:
#     print("python is not present.")


# Copy of file
# with open("this.txt") as f:
#     content  = f.read()
    
# with open("this_copy.txt", "w") as f:
#     f.write(content)
    
    
    
# with open("this.txt") as f:
#     content1  = f.read()
    
# with open("this_copy.txt") as f:
#     content2 = f.read()

# if(content1 == content2):
#     print("These file are identical.")
# else:
#     print("These file are not identical.")
    
    

# # To erase the file
# with open("this_copy.txt", "w") as f:
#     f.write(" ")
    
    

# To rename the file
with open("old.txt") as f:
    content = f.read()
    
with open("renamed_by_python.txt", "w") as f:
    f.write(content)