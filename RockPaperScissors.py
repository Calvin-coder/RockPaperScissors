import random

Check1 = 0
Check2 = 0

def win():
    if (MyPick == "Rock" and AIPick == "Scissors") or \
    (MyPick == "Paper" and AIPick == "Rock") or \
    (MyPick == "Scissors" and AIPick == "Paper"):
        Check1 == 1
        print("You win!!")

def draw():
   if MyPick == AIPick:
        Check2 == 1
        print("It's a draw!")

def lose():
    if Check1 or Check2 == 0:
        print("You lose!")

MyPick = input("Rock, Paper, or Scissors: ").capitalize()

while MyPick not in ["Rock", "Paper", "Scissors"]:
    MyPick = input("Input is not correct, please enter Rock, Paper, or Scissors: ").capitalize()

AIPick = random.choice(["Rock", "Paper", "Scissors"])
print(f"AI chose: {AIPick}")

win()
draw()
lose()
