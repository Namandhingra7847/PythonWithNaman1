from random import randint

number_to_guess = randint(1,100)
guess = None
attemps = 0

print("Wellcome to the Perfect Guess Game! ")
print("I have chosen a number between 1 and 100. Try to guess it. ")

while guess != number_to_guess:
    guess = int(input("Guess a Number: "))

    attemps +=1
    if guess > number_to_guess:
        print("Lower number please")
    elif guess < number_to_guess:
        print("Higher number please")
    else:
        print(f"Congratulations! You guess the right number {guess} in {attemps} attemps")