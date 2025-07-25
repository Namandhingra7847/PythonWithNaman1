def game():
    # Sample game function that returns a score
    # In real use, this would run a game and return the final score
    return int(input("Enter your game score: "))

# Get current score from game
score = game()

try: 
    # Try to read existing high score
    with open("Hi score.txt","r") as file:
        hiscore = file.read()
        if hiscore.strip():          # Check if file is not empty or just spaces
            hiscore = int(hiscore)   # Convert string to integer
        else:
            hiscore = 0              # Set default score to 0

except FileNotFoundError:
    hiscore = 0 # If file doesn't exist, assume high score is 0

# Compare and update high score if needed
if score > hiscore:
    print("Congratulation You got a new high score😎")
    with open("Hi score.txt","w") as file:
        file.write(str(score))
else:
    print("Try Again to beat your High Score🥲")

print(f"Your Score: {score} , High Score: {hiscore}")