import random

def win():
    print("You win!!")

def draw():
    print("It's a draw!")

def lose():
    print("You lose!")


MyPick = input("Rock, Paper, or Scissors: ").capitalize()

while MyPick not in ["Rock", "Paper", "Scissors"]:
    MyPick = input("Input is not correct, please enter Rock, Paper, or Scissors: ").capitalize()

AIPick = random.choice(["Rock", "Paper", "Scissors"])
print(f"AI chose: {AIPick}")

if MyPick == AIPick:
    draw()
elif (MyPick == "Rock" and AIPick == "Scissors") or \
     (MyPick == "Paper" and AIPick == "Rock") or \
     (MyPick == "Scissors" and AIPick == "Paper"):
    win()
else:
    lose()
