import random
import time
def TypingTest(type):
   sentences = {
    "easy": [
        "The quick brown fox jumps over the lazy dog while birds sing in the sky above.",
        "Learning Python can be fun and exciting if you practice it every single day.",
        "Typing fast requires focus and accuracy rather than just hitting keys randomly.",
        "A small puppy played happily in the garden chasing butterflies and barking loudly.",
        "The morning sun rises slowly bringing light warmth and hope for a new day.",
        "Books open the door to imagination and help people explore worlds beyond reality.",
        "A gentle breeze moved through the trees making the leaves dance and whisper softly.",
        "Children enjoy playing outside when the weather is sunny bright and comfortable.",
        "The river flows quietly between the mountains while fish swim happily in the water.",
        "Practice makes a person perfect and helps in improving their skills over time."
    ],

    "normal": [
        "Technology has changed the way humans communicate work and live creating endless opportunities but also challenges that society must address with responsibility\n and wisdom for future generations.",
        "The library was full of old dusty books yet it remained a peaceful sanctuary where students could concentrate read and discover knowledge that inspired them\n to learn and grow intellectually.",
        "Every successful person understands the importance of patience dedication and constant effort as these values eventually lead them to achieve their dreams\n despite facing countless struggles and failures along the way.",
        "The tall skyscrapers of the city shine brightly at night covered with millions of lights while cars buses and people move quickly creating a vibrant picture of\n urban life and progress.",
        "Nature always teaches valuable lessons to those who observe carefully such as resilience from trees strength from mountains and calmness from rivers flowing\n endlessly without expecting anything in return from anyone.",
        "The farmer works hard from dawn till dusk planting seeds watering the soil and ensuring his crops grow healthy so he can provide food to people across towns\n and cities nearby.",
        "During the cold winter season people gather near the fire drink warm soup share stories and feel the importance of family love and unity that keeps them\n strong throughout hardships.",
        "The ocean waves crash loudly against the rocks while seagulls fly above and ships move slowly across the horizon showing the vast power and mystery hidden\n within the deep sea.",
        "Education is considered the most powerful weapon that can change the world because it shapes thoughts inspires creativity and enables individuals to bring\n positive transformation in their communities and nations.",
        "Traveling opens the mind to different cultures languages foods and traditions making people realize the beauty of diversity and the importance of respecting one\n another across the globe peacefully."
    ],

    "hard": [
        "Scientific research continues to reveal fascinating truths about the universe from the smallest atoms to the largest galaxies reminding us that human knowledge\n is still limited and curiosity drives progress every single day across disciplines and cultures.",
        "In ancient civilizations people built massive structures like pyramids temples and palaces without modern technology proving their intelligence creativity and\n ability to work together for a common goal that still inspires engineers architects and historians across the globe.",
        "Global warming has become one of the most serious threats to humanity as rising temperatures melting glaciers and unpredictable weather patterns directly affect\n agriculture water supply wildlife and the very survival of future generations unless action is taken immediately.",
        "History has shown repeatedly that unity cooperation and understanding among nations can lead to long lasting peace while hatred division and greed only result \n in wars destruction and misery for millions of innocent people living across different continents worldwide.",
        "The invention of the printing press revolutionized human society because it allowed ideas stories and knowledge to be shared quickly leading to the spread of \n literacy education and scientific discoveries that shaped the modern world we live in today.",
        "Every human being carries within themselves the power to create change but this potential only comes alive when courage determination and faith overcome fear\n doubt and laziness which often stop individuals from pursuing their true purpose in life courageously.",
        "The human brain is the most complex organ ever studied with billions of neurons connecting in mysterious ways enabling people to think learn imagine remember\n and create extraordinary works of art science technology and culture across every part of history.",
        "Philosophers have long debated the meaning of life with some believing in destiny others in free will while many argue that happiness purpose and morality are\n what define existence and guide humanity through difficult choices in every era of civilization.",
        "The universe expands endlessly with countless stars planets and galaxies beyond what humans can see even with the most powerful telescopes raising questions\n about the possibility of life elsewhere and the origins of everything that exists in infinite space.",
        "Human progress depends not only on inventions and discoveries but also on ethics compassion and responsibility because without these values knowledge can be\n misused leading to harm destruction and suffering for individuals societies and the environment globally forever."
        ]
    }
   

   sentence = random.choice(sentences[type]) 
   print(sentence)
   starttime = time.time()
   usersentence = input("Type the sentence below :\n ")
   endtime = time.time()
   timeTaken = endtime - starttime

   #Accuracy
   original_words = sentence.split()
   typed_words = usersentence.split()
   correct_words = 0
   for i in range(min(len(original_words), len(typed_words))):
    if original_words[i] == typed_words[i]:
        correct_words += 1
   accuracy = (correct_words / len(original_words)) * 100

   #Wps
   totalwords = len(sentence.split(" "))    
   Wpm = (totalwords/timeTaken)*60

   #Result   
   print("✅ Time Taken: ",timeTaken , "seconds")
   print("🎯Accuracy:", accuracy, "%")
   print("⌨️ Speed:", round(Wpm, 2), "WPM")

    # Wrong words
   print("\n🔎 Mistakes:")
   for i in range(min(len(original_words), len(typed_words))):
        if original_words[i] != typed_words[i]:
            print(f"❌ Wrong: {typed_words[i]} 👉 Correct: {original_words[i]}")

    # Missed words
   if len(typed_words) < len(original_words):
        missed = original_words[len(typed_words):]
        for word in missed:
            print(f"⚠️ Missed word: {word}")

    # Extra words
   if len(typed_words) > len(original_words):
        extra = typed_words[len(original_words):]
        for word in extra:
            print(f"➕ Extra word typed: {word}")

            
#Main
print("---------Typing Test--------------")
print("1.Easy")
print("2.Normal")
print("3.Hard")
print("4.Exit")
try:
    while True:
      option = int(input("Enter option number to proceed:"))
      if option == 4:
         break
      if option == 1 :
         TypingTest("easy")
      if option == 2 :
         TypingTest("normal")
      if option == 3 :
         TypingTest("hard")
except ValueError:
   print("Enter option number")     