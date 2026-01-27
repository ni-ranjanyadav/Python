'''
1 for snake
-1 for water
0 for gun
'''
import random

computer = random.choice([-1,1,0])
youstr = input("Enter your choice: ").lower()

youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "snake", -1: "water", 0: "Gun"}

if youstr not in youDict:
    print("Invalid input! Please enter s, w, g")
else:
    you = youDict[youstr]

    print(f"you choose {reverseDict[you]}\ncomputer choose {reverseDict[computer]}")

    if(computer == you):
        print("It's Draw.")

    else:
        if(computer == -1 and you == 1):
            print("You Win!")
            
        elif(computer == -1 and you == 0):
            print("You Loss!")
            
        elif(computer == 1 and you == 0):
            print("You win!")
            
        elif(computer == 1 and you == -1):
            print("You Loss!")
            
        elif(computer == 0 and you == -1):
            print("You win!")
            
        elif(computer == 0 and you == 1):
            print("You Loss!")

        else:
            print("something went wrong")