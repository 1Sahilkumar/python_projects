import random
import threading

time_up = False  

def timeout():
    global time_up
    time_up = True
    print("\n⏰ Time's up!")
    
def Scramble():
    global time_up
    category = {
        "fruits": [
            "Apple", "Banana", "Mango", "Orange", "Grapes",
            "Pineapple", "Strawberry", "Watermelon", "Papaya", "Guava",
            "Cherry", "Peach", "Pear", "Plum", "Kiwi",
            "Pomegranate", "Lemon", "Coconut", "Lychee", "Apricot"
        ],
        "animals": [
            "Lion", "Tiger", "Elephant", "Giraffe", "Zebra",
            "Monkey", "Kangaroo", "Panda", "Leopard", "Cheetah",
            "Bear", "Wolf", "Fox", "Rabbit", "Horse",
            "Camel", "Goat", "Sheep", "Deer", "Dog"
        ],
        "countries": [
            "Pakistan", "India", "China", "Japan", "Nepal",
            "Bhutan", "Bangladesh", "SriLanka", "Afghanistan", "Iran",
            "Turkey", "SaudiArabia", "UAE", "Qatar", "Oman",
            "USA", "Canada", "Brazil", "Germany", "France"
        ]
    }

    points = 0
    while True:
        choose = input("\nEnter fruits, animals or countries (or 'exit' to leave): ").lower().strip()
        if choose == "exit":
            print("\nGame Over! Final Points:", points)
            break
        if choose not in category:
            print("❌ Wrong Choice. Try again.")
            continue

        word = random.choice(category[choose]).lower()
        shuffledWord = ''.join(random.sample(word, len(word)))
        print("\n🔀 Shuffled Word:", shuffledWord)

        chances = 3
        time_up = False
        timer = threading.Timer(15.0, timeout)
        timer.start()

        while chances > 0 and not time_up:
            guess = input("👉 Enter the correct word: ").lower().strip()
            if time_up:   
                print("💀 Out of time! The correct word was:", word.capitalize())
                break

            if guess == word:
                print("🎉 Correct! The word was:", word.capitalize())
                points += 1
                print("🏆 Your Points:", points)
                break
            else:
                chances -= 1
                print(f"❌ Wrong Guess. Chances left: {chances}")

        if chances == 0 and not time_up:
            print("💀 Out of chances! The correct word was:", word.capitalize())

        timer.cancel()

# Main program
print("1. Scramble Game")
print("2. Exit")

while True:
    try:
        option = int(input("\nEnter the option number: "))
        if option == 2:
            break
        if option == 1:
            Scramble()
        else:
            print("❌ Wrong option")
    except ValueError:
        print("⚠️ Please enter option number")
