import random
import time

computerScore = 0
playerScore = 0
totalPlays = 0
tie = 0
player2score = 0
player1score = 0


# function to generate dice roll
def dice_roll():
    global computerScore
    global playerScore
    global totalPlays
    global tie

    player = random.randint(1, 6)
    computer = random.randint(1, 6)
    totalPlays += 1
    print(f"player:{player} computer:{computer}")
    if player == computer:
        print("tie")
        tie += 1
    elif player > computer:
        print("you won!")
        playerScore += 1
    else:
        print("computer won!")
        computerScore += 1


def dice_roll_multiplayer():
    global player1score
    global player2score
    global totalPlays
    global tie
    input("player1 press enter to roll the dice")
    player1 = random.randint(1, 6)
    input("player1 press enter to roll the dice")
    player2 = random.randint(1, 6)
    totalPlays += 1
    print(f"player1:{player1} player2:{player2}")
    if player1 == player2:
        print("tie")
        tie += 1
    elif player1 > player2:
        print("player1 won!")
        player1score += 1
    else:
        print("player2 won!")
        player2score += 1


def stats(name1: str, name2: str, total, tie, name1score, name2score):
    print(f"total plays:{total}||tie:{tie}||{name1}:{name1score}||{name2}:{name2score}")
    if name1score > name2score:
        print(f"{name1} you won!")
    elif name1score == name2score:
        print("it's a draw!")
    else:
        print(f"{name2} you won!")


# function to print total score and repeat dice roll
def start(mode):
    if mode == 1:
        dice_roll()
    elif mode == 2:
        dice_roll_multiplayer()
    time.sleep(1)
    choice = input("do you want to roll the dice:")
    if choice == "":
        start(mode)
    else:
        if mode == 1:
            stats("computer", "player", totalPlays, tie, computerScore, playerScore)
        else:
            stats("player 1", "player 2", totalPlays, tie, player1score, player2score)


mode = int(input("enter 1 for single player|enter 2 for multiplayer:"))
start(mode)
with open("stats.txt","a+") as fptr:
    fptr.writelines("\ndate:"+time.ctime()+" | "+"playerscore:"+str(playerScore))
display = input("enter d to see your game history")
if display == "d":
    fptr = open("stats.txt", "r")
    print(fptr.readlines())
    fptr.close()


