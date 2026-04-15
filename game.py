import random

def stonepaperscissorgame():
    ROCK = 1
    PAPER = 2
    SCISSOR = 3
    EXIT = 4

    YOUR_SCORE = 0
    COMPUTER_SCORE = 0

    print("\n1. Select rock")
    print("2. Select paper")
    print("3. Select scissor")
    print("4. Exit")

    while True:
        me = int(input("\nEnter your choice from (1-4): "))

        if me == EXIT:
            print("\nGAME OVER")
            break

        computer = random.randint(1, 3)
        print(f"Computer choice is {computer}")

        if me == ROCK and computer == PAPER:
            print("\nYour choice is rock, Computer choice is paper **paper beats rock")
            print("YOU LOSE")
            COMPUTER_SCORE += 1
        elif me == ROCK and computer == SCISSOR:
            print("\nYour choice is rock, Computer choice is scissor **rock beats scissor")
            print("YOU WON")
            YOUR_SCORE += 1
        elif me == PAPER and computer == ROCK:
            print("\nYour choice is paper, Computer choice is rock **paper beats rock")
            print("YOU WON")
            YOUR_SCORE += 1
        elif me == PAPER and computer == SCISSOR:
            print("\nYour choice is paper, Computer choice is scissor **scissor beats paper")
            print("YOU LOSE")
            COMPUTER_SCORE += 1
        elif me == SCISSOR and computer == ROCK:
            print("\nYour choice is scissor, Computer choice is rock **rock beats scissor")
            print("YOU LOSE")
            COMPUTER_SCORE += 1
        elif me == SCISSOR and computer == PAPER:
            print("\nYour choice is scissor, Computer choice is paper **scissor beats paper")
            print("YOU WON")
            YOUR_SCORE += 1
        else:
            print("\nGAME DRAW")

        print("\n|---------------------------------------|")
        print("|           FINAL SCORE                 |")
        print("|---------------------------------------|")
        print(f"|YOUR SCORE IS {YOUR_SCORE} | COMPUTER SCORE IS {COMPUTER_SCORE}  |")
        print("|---------------------------------------|")

stonepaperscissorgame()
