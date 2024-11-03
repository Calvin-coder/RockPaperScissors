import random
#Win codition function
def win_condition():
    if (MyPick == "Rock" and AIPick == "Scissors") or \
    (MyPick == "Paper" and AIPick == "Rock") or \
    (MyPick == "Scissors" and AIPick == "Paper"):
        print("You win!!")
    elif MyPick == AIPick:
        print("It's a draw!")
    else:
        print("You lose!")

#Check if the player input in correct + Error code
MyPick = input("Rock, Paper, or Scissors: ").capitalize()
while MyPick not in ["Rock", "Paper", "Scissors"]:
    MyPick = input("Input is not correct, please enter Rock, Paper, or Scissors: ").capitalize()
#Picks the choice for the opponent
AIPick = random.choice(["Rock", "Paper", "Scissors"])
print(f"AI chose: {AIPick}")
#Plays the game
win_condition()
