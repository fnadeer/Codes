import random
number = random.randint(1,25)
num_guess = 0
while num_guess < 5:
    print('Guess a number between 1  and 25')
    guess = input()
    guess = int(guess)
    if guess == number:
        print("Cool your guess is correct")
        print("You nailed it on " + str(num_guess + 1) + " attempt")
        break
    if guess > number:
        print("Your guess is too high")
    if guess < number:
        print("Your guess is too low")
    num_guess += 1
    if num_guess == 5:
        print("Sorry you ran out of your guesses. The number was " + str(number))
