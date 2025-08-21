questions = [
    ["Who is Shahrukh Khan?", "Plumber", "Singer", "Wheslter", "Actor", 4],
    ["What is a capital of India?", "Mumbai", "Delhi", "Bangalore", "Gurgoan", 2],
    ["Which planet is known as Red Planet?", "Earth", "Mars", "Venus", "Jupiter", 2],
    ["Who Developed Python>", "Guido Van Rossum", "Dennis Richil", "Bjarne Stoustroup", "James Gosling",1],
    ["Who Developed Java?", "Guido Van Roosum", "Dennis Richil", "Bjarne Stoustroup", "James Gosling",4],
    ["What is Square root of 64?", "6", "10", "8", "12", 3],
    ["Which one is the fastest land Animal?", "Lion", "Cheetah", "Elephant", "horse", 2],
]
prizes = [10000, 50000, 100000, 500000, 1000000, 5000000, 10000000]

print("👋🏻Wellcome to Who Wants to be a Millionare💸\n")

i = 0

for  question in questions:
    print(question[0])
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}")

    # check whether the answer is correct or not.
    
    b = int(input("Enter your answer (1/2/3/4): "))

    if (question[5] == b):
        print(f"Answer is Correct👍! You have won ${prizes[i]}\n")
    else:
        print(f"Incorrect😔, The Answer is {question[5]}")
        print("Better luck next time!")
        break
    i+=1
else:
    print("Congratulation🥳! You answered all questions and became a Crorepati💸!\n")



