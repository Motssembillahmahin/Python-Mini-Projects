import random

word_choice = ["Mahin", "Robi", "Shawon"]

choose_word = random.choice(word_choice).lower()
print(choose_word)
display = ["_"]
display *= len(choose_word)
lives = 6

end_of_game = False
while not end_of_game:
    guess_word = input("Enter a letter ").lower()
    for x in range(0, len(choose_word)):
        if choose_word[x] == guess_word:
            display[x] = guess_word
    print("You're choosing  a wrong number")
    print(display)
    if guess_word not in choose_word:
        lives -= 1
        print(f"Your remaining life is {lives}")
        if lives == 0:
            end_of_game = True
            print("You loose")

    if '_' not in display:
        end_of_game = True
        print("You win")
