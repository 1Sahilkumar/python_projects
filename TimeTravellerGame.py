machineparts = ["part1","part2","part3","part4","part5"]

parts = []
#Time Zone 1:
def AncientEgypt():
    global parts
    if "part1" in  parts:
        print("You already got part from this time Zone")
        return
    else:
        print("Five torches stand before you: [North, South, East, West]")
        print("The ancient rune glows: \n[First comes the east,\nthen the flame of double the west,\nthen the one that guards the north, \nand at last, the torch that is 3rd in line.]  ")
        pattern = ["East","West","West","North","North"]
        EnterPattern = input("Enter torch sequence (5 steps) separated by commas:")
        seperated = [x.strip().capitalize() for x in EnterPattern.split(",")] 
        if seperated == pattern:
            print("The torches ignite in order, the cave rumbles, and the gate opens!")
            print("You picked machine piece!")
            parts.append("part1")
            print(f"Now you have {len(parts)} machine parts")
            print("Returning to timeline menu")
        else:
            print("The flames die out.")
            print("Kicked Out of This TimeLine.")  
#Time Zone 2:        
def MedievalAge():
    global parts
    if "part2" in parts:
        print("You already got part from this time Zone")
        return
    else:

        print("\n⛪ You arrive at an old stone keep guarded by a silent sentry.")
        print("A weathered plaque reads:\n")
        print('"Only one who knows the land may pass.\n'
            'Answer me this riddle and the gate will yield:\n"')
        print("  \"I have cities, but no houses.\n"
            "   I have mountains, but no trees.\n"
            "   I have water, but no fish.\n"
            "   What am I?\"\n")

        answer = input("Your answer: ").strip().lower()
        valid_answers = {"map", "a map", "the map"}

        if answer in valid_answers:
            print("\nThe stone guardians nod. The gate grinds open.")
            print("Inside you find a gleaming machine piece!")
            parts.append("part2")
            print(f"Now you have {len(parts)} machine parts.")
            print("Returning to timeline menu")
            return
        else:
            print("\nThe guardians roar and the gate slams shut.")
            print("You are Kicked Out of this TimeLine.")
            return
#Time Zone 3:        
def IndustrialAge():
    global parts
    if "part3" in parts:
        print("You already got part from this time Zone")
        return
    else:

        print("You Entered a Large Industry with a large gear based Door.TO open that door you have to solve a puzzle")
        print("Hint:5-2 = 3 ,12-5 = 7 ")
        puzzle = input("Guess The missing : 2, 5, 12, __, 30 :")
        if puzzle == "23":
            print("The gears rotates and the door opened.")
            print("You picked the part of the machine !")
            parts.append("part3")
            print(f"Now you have {len(parts)} machine parts") 
            print("Returning to timeline menu")
        else:
            print("Wrong Answer")
            print("You are kicked from this TimeZone")

#Time Zone 4            
def Future2050():
    global parts
    if "part4" in parts:
        print("You already got part from this time Zone")
        return
    else:
        Fab = ["0","1","1","10","11","101","1000","1101","10101","100010","110111"]
        print("You are in a lab.The Door is locked .To unlock the door you have to complete the code.")
        print("Hint: Fibonacci in binary")
        series = input("0,_,1,_,_,_11,101,_,_,_,_,110111.Complete the Series(Rewrite the given one too)Seperated by commas:")
        seperated = [x.strip() for x in series.split(",")]
        if seperated == Fab:
            print("Correct Series.Door Opened")
            print("You picked the part of the machine !")
            parts.append("part4")
            print(f"Now you have {len(parts)} machine parts")
            print("Returning to timeline menu")
        else:
            print("Wrong Series")     
            print("You are kicked from this TimeZone")

#Time Zone 5:           
def PostApocalypse():
   global parts
   if "part5" in parts:
       print("You already got part from this time Zone")
       return
   else:
    questions = [
        {
            "question": "What type of radiation consists of high-energy photons?",
            "options": ["Alpha rays", "Beta rays", "Gamma rays", "Neutrons"],
            "answer": 3
        },
        {
            "question": "Which type of radiation can be stopped by a sheet of paper?",
            "options": ["Alpha", "Beta", "Gamma", "Neutron"],
            "answer": 1
        },
        {
            "question": "Which radiation particle has a negative charge?",
            "options": ["Alpha", "Beta", "Gamma", "Neutron"],
            "answer": 2
        },
        {
            "question": "What is the unit used to measure absorbed radiation dose?",
            "options": ["Sievert", "Gray", "Curie", "Becquerel"],
            "answer": 2
        },
        {
            "question": "Which material is most effective at blocking gamma radiation?",
            "options": ["Aluminum", "Lead", "Plastic", "Glass"],
            "answer": 2
        },
        {
            "question": "Which radiation is emitted from Helium nuclei?",
            "options": ["Alpha", "Beta", "Gamma", "X-ray"],
            "answer": 1
        },
        {
            "question": "What does 'half-life' of a radioactive isotope mean?",
            "options": [
                "Time taken for all atoms to decay",
                "Time for activity to double",
                "Time for half of the atoms to decay",
                "Time for energy to reduce to zero"
            ],
            "answer": 3
        },
        {
            "question": "Which device is commonly used to detect radiation?",
            "options": ["Thermometer", "Geiger-Müller counter", "Barometer", "Microscope"],
            "answer": 2
        },
        {
            "question": "Which type of radiation is most penetrating?",
            "options": ["Alpha", "Beta", "Gamma", "All are equal"],
            "answer": 3
        },
        {
            "question": "Which radiation unit measures biological damage in humans?",
            "options": ["Gray", "Sievert", "Becquerel", "Curie"],
            "answer": 2
        }
    ]

    score = 0
    print("You are in the time of PostApocalypse.But still there are some virus cases.You got Infected by virus.SObefore going \n for machine part you have to get antidot. You entered in a lab for an antidot but it is locked. \n To unlock the lab you have to answer all the question correctly. \n")
    for q in questions:  
                print("\n" + q["question"])
                for i, opt in enumerate(q["options"], start=1):  
                    print(f"{i}. {opt}")
                    

                ans = int(input("Enter your answer: "))

                if ans == q["answer"]:
                    print("Correct!")
                    score += 1

                else:
                    print(f"Wrong! Correct answer is: {q['answer']}")
    if score < 10:
            print("You not got all answer Correct.")
            print("You are kicked from this TimeZone")
    else:
        pattern = ["Blue","Yellow","Red","Green"]    
        print("Weldone you break through the virus.Now it time to get the key.")
        print("You find a locked chest with different colors you have to write them in correct patterns.")
        print("Blue before Red, but never after Yellow. Green must come last")
        puzzle = input("Enter the correct pattern of colors(Red, Blue, Green, Yellow.) to unlock the chest seperated by commas:")
        seperated = [x.strip().capitalize() for x in puzzle.split(",")] 
        if seperated == pattern:
            print("The Chest opens!")
            print("You picked machine piece!")
            parts.append("part5")
            print(f"Now you have {len(parts)} machine parts")
            print("Returning to timeline menu")
        else:
            print("You wrote the wrong pattern.")
            print("Kicked Out of This TimeLine.")       

print("One Day you were travelling through the jungle and you found a oval shaped machine.\n" \
"You excitedly entered the machine and clicked a button then suddenly machine started levitating and disappeared with you in time.\n" \
"Due to the sudden levitating you got fainted.When you got up you saw on screen that this machine travelled through \n" \
"5 different time zones and got damaged.Its parts dropped in all those time zones.You have to find them and repair the machine\n" \
"to go to your Time Zone.")
print("1.Ancient Egypt")
print("2.Medieval Age")
print("3.Industrial Age")
print("4.Future 2050")
print("5.Post-Apocalypse")
print("6.Exit")


while True:
        if set(parts) == set(machineparts):
            print("Weldone You got all Machine part.")
            print("🚀 MACHINE REPAIRED 🚀")
            print("You successfully traveled back to your time.")
            break
        try:
            choose=int(input("\n choose option to go to that time:"))
            if choose == 6:
                break
            if choose == 1:
                AncientEgypt()
            elif choose == 2:
                MedievalAge()
            elif choose == 3:
                IndustrialAge()
            elif choose == 4:
                Future2050()
            elif choose == 5:
                PostApocalypse()
            else:
                print("Wrong choice")
        except ValueError:
            print("Enter option number")