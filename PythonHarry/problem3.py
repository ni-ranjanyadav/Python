import os

# Get current working directory
path = os.getcwd()

# List all files and folders
contents = os.listdir(path)

print("Contents of the directory:")
for item in contents:
    print(item)



import os

path = "C:/Users"   # change this path as needed

print("Contents of the directory:")
for item in os.listdir(path):
    print(item)
