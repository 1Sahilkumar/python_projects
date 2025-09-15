import random 

def Game():
    shapes = ["rock", "paper", "scissors"]
    userwin = 0
    computerwin = 0

    while True:
        randomnum = random.randint(0, 2)
        computer = shapes[randomnum]
        player = input("Enter rock, paper or scissors (q to quit): ").lower()

        if player == "q":
            break

        if player not in shapes:
            print("Invalid choice, try again.")
            continue

        print("You chose:", player)
        print("Computer chose:", computer)

        if (player == "rock" and computer == "scissors") or \
           (player == "paper" and computer == "rock") or \
           (player == "scissors" and computer == "paper"):
            print("You won!")
            userwin += 1
        elif player == computer:
            print("Game Tie")
        else:
            print("You lost")
            computerwin += 1

        print(f"Score: You = {userwin}, Computer = {computerwin}\n")

    print("\n Final Result:")
    print(f"You: {userwin} | Computer: {computerwin}")
    if userwin > computerwin:
        print(" Congratulations! You are the winner.")
    elif userwin < computerwin:
        print(" Computer wins!")
    else:
        print("It's a tie!")


while True:
    wannaplay = input("Do you wanna play? (yes/no): ").lower()
    if wannaplay == "yes":
        Game()
    else:
        print("Goodbye")
        break
