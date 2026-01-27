import random

n = random.randint(1, 100)
a = -1
guesses = 0

while(a != n):
    try:
        a = int(input("Guess a number: "))
        guesses += 1
        
        if(a > n):
            print("Lower number please")
        else:
            print("Higher number please")
            
    except ValueError:
        print("Please Enter a valid number.")
            
print(f"You have gussed the number {n} correctly in {guesses} attempt")
