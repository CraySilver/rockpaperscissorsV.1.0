import random

ai_answer = (random.randrange (1, 4))

your_answer = input("What move would you like to do?:")

print("You: " +str(your_answer))

if (ai_answer == 1):
    print("AI: Rock")

if (ai_answer == 2):
    print("AI: Paper")

if (ai_answer == 3):
    print("AI: Scissors")

if (ai_answer == 3 and your_answer == "rock" ):
        print("You Win!")
if (ai_answer == 1 and your_answer == "rock"):
        print("Tie try again!")
if (ai_answer == 2 and your_answer == "rock" ):
        print("You lost!")

if (ai_answer == 2 and your_answer == "paper"):
        print("Tie try again!")
if (ai_answer == 3 and your_answer == "paper" ):
        print("You lost!")
if (ai_answer == 1 and your_answer == "paper" ):
        print("You Win!")

if (ai_answer == 3 and your_answer == "scissors"):
        print("Tie try again!")
if (ai_answer == 1 and your_answer == "scissors" ):
        print("You lost!")
if (ai_answer == 2 and your_answer == "scissors" ):
        print("You Win!")



