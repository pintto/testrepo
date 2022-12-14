import random


def print_scores():
    print("Player 1 score:", player1Score, "points")
    print("player 2 score:", player2Score, "points")


def play_again():
    play_over = input("\nPlay again? (y/n): ")
    user_reply = ["n", "N", "no", "No"]
    if play_over in user_reply:
        print("Game Over")
        exit()


def reset_scores():
    global player1Score, player2Score
    player1Score = 0
    player2Score = 0


moves = ["Rock", "Paper", "Scissors"]

player1Score = 0
player2Score = 0

print("\nE P I C    🪨  📄 ✂️    B A T T L E \n")

while True:
    player1Move = random.choice(moves)
    player2Move = random.choice(moves)

    print("Player 1 move is:", player1Move)
    print("Player 2 move is:", player2Move, "\n")

    if player1Move == "Rock":
        if player2Move == "Rock":
            print("You both picked Rock, draw!")
        elif player2Move == "Scissors":
            player1Score += 1
            print("Player 1 smashed Player's 2 Scissors into dust with their Rock!\nWinner: Player 1!")
            print_scores()
        else:
            print("Player's 1 Rock is smothered by Player's 2 Paper!\nWinner: Player 2!")
            player2Score += 1
            print_scores()

    elif player1Move == "Paper":
        if player2Move == "Rock":
            player1Score += 1
            print("Player's 2 Rock is smothered by Player's 1 Paper!\nWinner: Player 1!")
            print_scores()
        elif player2Move == "Scissors":
            player2Score += 1
            print("Player's 1 Paper is cut into tiny pieces by Player's 2 Scissors!\nWinner: Player 2!")
            print_scores()
        else:
            print("Two bits of paper flap at each other. Disappointing. Draw.")

    else:
        if player2Move == "Rock":
            player2Score += 1
            print("Player's 2 Rock makes metal-dust out of Player's 1 Scissors\nWinner: Player 2!")
            print_scores()
        elif player2Move == "Scissors":
            print("Ka-Shing! Scissors bounce off each other like a dodgy sword fight! Draw.")
        else:
            player1Score += 1
            print("Player's 1 Scissors make confetti out of Player's 2 paper!\nWinner: Player 1!")
            print_scores()

    if player1Score == 3:
        print("\nPlayer 1 won. Game over")
        print_scores()
        reset_scores()
        play_again()

    elif player2Score == 3:
        print("\nPlayer 2 won. Game over")
        print_scores()
        reset_scores()
        play_again()

    else:
        play_again()


