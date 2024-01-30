import random

easy_attempts = 10
hard_attempts = 5

turns = 0


def check(guess, randomly_gussing_number, turns):
    if guess > randomly_gussing_number:
        print("Too high")
        return turns - 1
    elif guess < randomly_gussing_number:
        print("Too low")
        return turns - 1
    else:
        print(f"You got the right answer! The right number is {randomly_gussing_number}")


def set_difficulty():
    choose_level = input("choose difficulty type 'easy' or 'hard' ")
    if choose_level == 'easy':
        return easy_attempts
    elif choose_level == 'hard':
        return hard_attempts
    else:
        return set_difficulty()



def game():
    print("Wellcome to the Number guessing game!")
    print("I'm thinking a number between 1 to 100 ")
    randomly_guessing_number = random.randint(1, 100)
    print(randomly_guessing_number)
    turns = set_difficulty()

    guess = 0
    while guess != randomly_guessing_number:
        print(f"You have remaining {turns}")
        guess = int(input("Make a guess "))
        turns = check(guess, randomly_guessing_number, turns)
        if turns == 0:
            print("You are running out of your attempts, you're lose!")
            break



game()
