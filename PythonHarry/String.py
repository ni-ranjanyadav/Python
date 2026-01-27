name = "Niranjan Kumar"
print(len(name))
name_short = name[0:3]
print(name_short)

#Negative Slicing
print(name[-14:])
print(name[0:14])
print(name[1:])
print(name[:4]) 

# Escape Sequence Character
# \n - New line, \t - tab, \' - single quote , \\ - backslash

name = input("Enter your name: ")
print("Good afternoon",name)
print(f"Good afternoon {name}")