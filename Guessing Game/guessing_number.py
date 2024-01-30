import random
print("Wellcome to the Number guessing game!")
print("I'm thinking a number between 1 to 100 ")
randomly_gussing_number = random.randint(1, 100)
print(randomly_gussing_number)
easy_attempts = 10
hard_attempts = 5


def easy():
    global randomly_gussing_number, easy_attempts;
    terminate_easy_function = True
    while terminate_easy_function:
        print(f"You've {easy_attempts} remaining to guess the number.")
        gussing_number = int(input("Make a guess"))
        correct_gusssing_number = True
        while correct_gusssing_number :
            if gussing_number != randomly_gussing_number:
                if gussing_number > randomly_gussing_number:
                    print("Too high")
                    return easy_attempts - 1
                elif gussing_number < randomly_gussing_number:
                    print("Too low")
                    return easy_attempts - 1


            elif gussing_number == randomly_gussing_number:
                print("You got the right answer")
                return
            if gussing_number == randomly_gussing_number or easy_attempts == 0 :
                correct_gusssing_number = False

        #if easy_attempts == 0:
            #terminate_easy_function = False
choose_level = input("choose difficulty type 'easy' or 'hard' ")
if choose_level  == 'easy' :
    easy()
elif choose_level  == 'hard':
    print("This is hard point")
else :
    print("You typed wrong keyword ")


