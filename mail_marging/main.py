

placeholder = "[name]"

with open('./Input/Names/invited_names.txt') as data:
    names = data.readlines()
with open('./Input/Letters/starting_letter.txt') as word :
    follow_letter = word.read()
    for nam in names:
        stripped_letter = nam.strip()
        new_letter = follow_letter.replace(placeholder, stripped_letter)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_letter}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)


list = [1, 3, 5, 7, 9, 11]
print(list[-1:0:-2])