import random
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
generating_output = random.randint(0,2)
print(user_input)
print(generating_output)
#O, FOR ROCK
if user_input == 0 and generating_output == 2 :
    print("You win")
elif generating_output > user_input :
    print("You lose")
elif user_input == generating_output :
    print("Draw")
else:
    print("You lose")