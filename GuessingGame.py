import random


def WordGuess():
    hangman_stages = {
        0: """
         -----
         |   |
         |
         |
         |
         |
        _|_
        """,
        1: """
         -----
         |   |
         |   O
         |
         |
         |
        _|_
        """,
        2: """
         -----
         |   |
         |   O
         |   |
         |
         |
        _|_
        """,
        3: """
         -----
         |   |
         |   O
         |  /|
         |
         |
        _|_
        """,
        4: """
         -----
         |   |
         |   O
         |  /|\\
         |
         |
        _|_
        """,
        5: """
         -----
         |   |
         |   O
         |  /|\\
         |  /
         |
        _|_
        """,
        6: """
         -----
         |   |
         |   O
         |  /|\\
         |  / \\
         |
        _|_
        """
    }

    category = {
        "fruits": [
            "Apple", "Banana", "Mango", "Orange", "Grapes",
            "Pineapple", "Strawberry", "Watermelon", "Papaya", "Guava"
        ],
        "vegetables": [
            "Carrot", "Potato", "Tomato", "Cabbage", "Spinach",
            "Onion", "Broccoli", "Cauliflower", "Cucumber", "Peas"
        ],
        "dryfruits": [
            "Almond", "Cashew", "Pistachio", "Walnut", "Raisin",
            "Fig", "Date", "Hazelnut", "Peanut", "Apricot"
        ]
    }

    while True:
        chooseCategory = input("Enter Category from [fruits, vegetables, dryfruits] or exit : ").lower().strip()
        if chooseCategory == "exit":
            break
        if chooseCategory not in category:
            print("❌ Wrong choice! Try again.")
            continue

        word = random.choice(category[chooseCategory]).lower()
        chances = 6
        guessed = ["_"] * len(word)
        used_letters = []

        print(f"\nHangman Game - Category: {chooseCategory.capitalize()}")
        print(hangman_stages[chances])

        while chances > 0:
            print("\nWord to guess: ", " ".join(guessed))
            print("Used letters:", ", ".join(used_letters))
            guess = input("Guess a letter or type 'exit': ").lower().strip()

            if guess == "exit":
                print("Exiting this round...\n")
                break

            if len(guess) != 1 or not guess.isalpha():
                print("❌ Enter only a single letter!")
                continue

            if guess in used_letters:
                print("⚠️ You already used this letter.")
                continue

            used_letters.append(guess)

            if guess in word:
                for i, ch in enumerate(word):
                    if ch == guess:
                        guessed[i] = guess
                if "_" not in guessed:
                    print("\n🎉 Congratulations! You guessed the word:", word.capitalize())
                    break
            else:
                chances -= 1
                print("\nWrong guess!")
                print(hangman_stages[chances])

        if chances == 0:
            print("💀 You killed the man! The word was:", word.capitalize())

def GuessNumber():
    point = 0
    while True:
        choose = input("Enter 'easy','normal' or 'hard' or exit :").lower().strip()
        if choose == "exit":
            break      
        if choose == "easy":
            chances = 3
            easy = random.randint(1,10)
            while chances > 0:                  
                    easyguess = int(input("Guess the number between 1-10 or 0 to leave:"))
                    if easyguess == 0:
                        break
                    if easyguess == easy:
                        print("Correct")
                        point += 1
                        print("Points: ", point)
                    elif easyguess < easy:
                        print("Your guess is low")
                    else:
                            print("Your guess is high")
                    chances -= 1 
            if chances == 0:
                print("Out of chances.Correct Number was :",easy)        
        elif choose == "normal":
            chances = 5
            Normal = random.randint(1,50)
            while chances > 0:                  
                    Normalguess = int(input("Guess the number between 1-50 or 0 to leave:"))
                    if Normalguess == 0:
                        break
                    if Normalguess == Normal:
                        print("Correct")
                        point += 1
                        print("Points: ", point)
                    elif Normalguess < Normal:
                        print("Your guess is low")
                    else:
                            print("Your guess is high")
                    chances -= 1 
            if chances == 0:
                print("Out of chances.Correct Number was :",Normal)             
        elif choose == "hard":
             chances = 7
             Hard = random.randint(1,100)
             while chances > 0:                  
                    Hardguess = int(input("Guess the number between 1-100 or 0 to leave:"))
                    if Hardguess == 0:
                        break
                    if Hardguess == Hard:
                        print("Correct")
                        point += 1
                        print("Points: ", point)
                    elif Hardguess < Hard:
                        print("Your guess is low")
                    else:
                            print("Your guess is high")
                    chances -= 1 
             if chances == 0:
                print("Out of chances.Correct Number was :",Hard)        



#Main program:
print("1.Word Guessing Game")
print("2.Number Guessing Game")
print("3.Exit")            

while True:
    try:
        choose = int(input("Enter option number:"))
        if choose == 3:
            break
        if choose == 1:
            WordGuess()
        elif choose == 2:
            GuessNumber()
        else:
            print("Enter option number between 1-3")        
    except ValueError:
        print("Enter Number value please...")