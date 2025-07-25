from random import randint

n = randint(1,100)

a = None
guesses = 0
while(a != n):
    a = int(input("Guess a Number: "))
    guesses += 1 
    if(a > n):
        print("Lower number please")
    else:
        print("Higher number please")

print(f"you guess the right number {n} in {guesses} attemps ")

