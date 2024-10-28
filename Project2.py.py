import random
computer = random.choice([1,2,3])
print("WELCOME to Stone , Paper, Scissor Game ;) ")
user = input("Enter your choice: ").capitalize()
dict1={ 1 : "Stone", 2 : "Paper", 3 : "Scissor"}
print(f"Computer chose: {dict1[computer]}")
asignDict={"Stone": 1 ,"Paper" : 2 ,"Scissor" : 3}
if user in asignDict:
    you = asignDict[user]
    if((computer == 1 and you == 2) or (computer == 2 and you == 3) or (computer == 3 and you == 1)):
        print("HOORAY! you won ;)")
    elif((computer == 1 and you == 3) or (computer == 2 and you == 1) or (computer == 3 and you == 2)):
        print("Loser!!! better luck next time")
    else:
        print("Its a draw!!")
else:
    ("INVALID!! please enter stone, paper or scissor")