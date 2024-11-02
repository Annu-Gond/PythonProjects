import random
print("WELCOM TO NUMBER GUESSING GAME!!!")
n = -1
guess = 1
a = random.randint(1,100)
while(a!= n):
    n = int(input("Guess the correct nuumber:"))
    if(a < n):
        print("Lower number please")
        guess += 1

    elif(a > n):
        print("Higher number please")
        guess += 1

print(f"You have guessed the right number {a} in {guess} guesses")