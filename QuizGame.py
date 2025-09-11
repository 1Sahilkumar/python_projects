import time
questions = [
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["func", "def", "function", "define"],
        "answer": 2
    },
    {
        "question": "What is the output of: print(type([])) ?",
        "options": ["dict", "list", "tuple", "set"],
        "answer": 2
    },
    {
        "question": "Which of the following is immutable?",
        "options": ["List", "Set", "Dictionary", "Tuple"],
        "answer": 4
    },
    {
        "question": "Which operator is used for exponentiation in Python?",
        "options": ["^", "**", "pow", "//"],
        "answer": 2
    },
    {
        "question": "What is the default return type of input() in Python?",
        "options": ["int", "float", "string", "bool"],
        "answer": 3
    },
    {
        "question": "Which module in Python is used for random numbers?",
        "options": ["math", "os", "random", "sys"],
        "answer": 3
    },
    {
        "question": "Which keyword is used to create a class in Python?",
        "options": ["function", "define", "class", "object"],
        "answer": 3
    },
    {
        "question": "What is the output of: bool('False') ?",
        "options": ["True", "False", "None", "Error"],
        "answer": 1
    },
    {
        "question": "Which of the following is not a valid Python data type?",
        "options": ["List", "Array", "Tuple", "Set"],
        "answer": 2
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["//", "/* */", "#", "--"],
        "answer": 3
    },
    {
        "question": "What is the output of: print(2 == 2.0)?",
        "options": ["True", "False", "Error", "None"],
        "answer": 1
    },
    {
        "question": "Which keyword is used to handle exceptions in Python?",
        "options": ["catch", "except", "error", "try"],
        "answer": 2
    },
    {
        "question": "What is the correct file extension for Python files?",
        "options": [".pt", ".pyt", ".py", ".pyth"],
        "answer": 3
    },
    {
        "question": "Which function is used to get the length of a list in Python?",
        "options": ["count()", "length()", "size()", "len()"],
        "answer": 4
    },
    {
        "question": "Which of the following is used to define a block of code in Python?",
        "options": ["Curly Braces {}", "Indentation", "Parentheses ()", "Square Brackets []"],
        "answer": 2
    },
    {
        "question": "What is the output of: print('Hello' * 3)?",
        "options": ["Hello3", "HelloHelloHello", "Error", "3Hello"],
        "answer": 2
    },
    {
        "question": "Which built-in data type is a sequence in Python?",
        "options": ["List", "Dictionary", "Set", "All of the above"],
        "answer": 1
    },
    {
        "question": "Which keyword is used to stop a loop in Python?",
        "options": ["stop", "break", "exit", "quit"],
        "answer": 2
    },
    {
        "question": "What is the output of: print(type({}))?",
        "options": ["dict", "set", "list", "tuple"],
        "answer": 1
    },
    {
        "question": "Which function is used to read input from the user?",
        "options": ["get()", "input()", "scan()", "read()"],
        "answer": 2
    },
    {
        "question": "Which keyword is used to check conditions in Python?",
        "options": ["if", "when", "for", "switch"],
        "answer": 1
    },
    {
        "question": "What is the output of: print(10 // 3)?",
        "options": ["3.33", "3", "4", "Error"],
        "answer": 2
    },
    {
        "question": "Which function is used to convert a string to an integer?",
        "options": ["str()", "int()", "float()", "eval()"],
        "answer": 2
    },
    {
        "question": "What is the output of: print(bool(0))?",
        "options": ["True", "False", "None", "Error"],
        "answer": 2
    },
    {
        "question": "Which data type is returned by the input() function?",
        "options": ["int", "float", "string", "bool"],
        "answer": 3
    },
    {
        "question": "Which of the following is used to define a function in Python?",
        "options": ["func", "def", "lambda", "function"],
        "answer": 2
    },
    {
        "question": "Which operator is used to check equality in Python?",
        "options": ["=", "==", "!=", "<>"],
        "answer": 2
    },
    {
        "question": "What is the output of: print(type(3.0))?",
        "options": ["int", "float", "double", "decimal"],
        "answer": 2
    },
    {
        "question": "Which keyword is used to return a value from a function?",
        "options": ["return", "break", "yield", "stop"],
        "answer": 1
    },
    {
        "question": "Which of the following is a mutable data type?",
        "options": ["Tuple", "List", "String", "FrozenSet"],
        "answer": 2
    }
]



print("--------------Python Quiz Game ---------------------")
print("1. Start Game:")
print("2. Exit")

score = 0
while True:
    option = int(input("Enter any option : " ))
    if option == 1:
        start = time.time()
        for q in questions:  
            print("\n" + q["question"])
            for i, opt in enumerate(q["options"], start=1):  
                print(f"{i}. {opt}")
                

            ans = int(input("Enter your answer: "))

            if ans == q["answer"]:
                print("✅ Correct!")
                score += 1

            else:
                print(f"❌ Wrong! Correct answer is: {q['answer']}")
        end = time.time()  
        print("\nQuiz Finished!")
        print("You took", end - start, "seconds to answer")
        print(f"Your Score: {score}/{len(questions)}")
      
    elif option == 2:
        break
    else:
        print("Wrong Option")
 