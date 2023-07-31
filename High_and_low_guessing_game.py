import random

highest_value = 0
lowest_value = 0

difficulty = input("Choose a difficulty level (Easy, Medium, Hard, Legendary): ")

if difficulty.lower() == "easy":
    highest_value = 10
    lowest_value = 1
elif difficulty.lower() == "medium":
    highest_value = 100
    lowest_value = 1
elif difficulty.lower() == "hard":
    highest_value = 500
    lowest_value = 1
elif difficulty.lower() == "legendary":
    highest_value = 1000
    lowest_value = 1

target_number = random.randint(lowest_value, highest_value)
print("Guess a number between", lowest_value, "and", highest_value)

num_guesses = 0
max_guesses = 10

while num_guesses < max_guesses:
    guess = int(input("Please enter your guess: "))
    num_guesses += 1

    if guess < target_number:
        print("Too low!")
    elif guess > target_number:
        print("Too high!")
    else:
        print("Congratulations, You guessed the number in", num_guesses, "guesses.")
        break

if num_guesses >= max_guesses:
    print("Sorry, you just run out of your", max_guesses,
          "possible guesses. The number was", target_number, ".To continue please rerun the program.")