import random

cards = [11, 2, 3, 4, 5, 6, 7, 9, 10, 10, 10, 10]


def choice_card():
    player = random.sample(cards, k=2)
    computer_player = random.choice(cards)
    computer = [computer_player]
    return player, computer


# another card
player1, comp = list(choice_card())
print(f"The list of player {player1} ")
print(f"The list of Computer provide valur {comp} ")
total_player_2_card = sum(player1)
print(f"player total of first two card {total_player_2_card} ")


def computer_all():
    want_stop = True
    while want_stop:
        computer_another_card = random.choice(cards)
        comp.append(computer_another_card)
        total_computer_Card_value = sum(comp)
        print(f"The value of computer card {total_computer_Card_value} ")
        print(total_computer_Card_value)
        if total_computer_Card_value > 21 :
            want_stop = False
    return total_computer_Card_value


excced_value = True
while excced_value:
    if input(f"Would you like to opt another card, if yes then press 'y' or pass 'n' ") == 'y':
        player_another_card = random.choice(cards)
        player1.insert(2, player_another_card)
        after_adding_another_card = sum(player1)
        print(f"List after adding another card {player1} ")
        print(f"after adding another card {after_adding_another_card}")
        if after_adding_another_card > 21:
            print("You lose")
            excced_value = False
        elif input(f"Are you want to stand in  game, then press y or wish to continue then type n") == 'y':
            print(f"Player standing value with {after_adding_another_card} ")
            computer_all()
            excced_value = False
        else:
            continue
    else:
        print(player1)
        print(f"Player standing with first 2 card {total_player_2_card} ")
        computer_all()
        excced_value = False



