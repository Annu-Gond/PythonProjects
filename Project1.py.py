import random
computer = random.choice([1,0,-1])
print("WELCOME to Snake , Water ,Gun")
user = input("Enter your choice:").capitalize()
dict1 ={ 1 : "Water", 0 : "Snake", -1 : "Gun"}
print(f"Computer's choice: {dict1[computer]}")
asignDict ={"Water" : 1 , "Snake" : 0 , "Gun" : -1}
if user in asignDict :
    you = asignDict[user]
    if((computer == 1 and you == 0) or (computer == 0 and you == -1) or (computer== -1 and you == 1)):
        print("HOORAY ! You won ;)")
    elif((computer == -1 and you == 0) or (computer == 1 and you == -1) or (computer== 0 and you == 1)):
        print("Oh No ! you have lost :(")
    else:
        print(" LOL!,Its a tie -_-")    
else:
    print("Invalid ! Please enter snake , water or gun")