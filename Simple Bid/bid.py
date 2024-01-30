list = []
dict = {}

want_or_not = True
while (want_or_not != False):
    want_or_not = input("Would you like to apply on bid : y/n? \n")

    if want_or_not == 'y':
        name = input("what is your name? \n")
        bid_value = int(input("what is your bid \n"))
        dict[name] = bid_value

        #print(dict)
    else:
        want_or_not = False

highest_bid = 0
winner = ""
for bidder in dict :
    bit_amount = dict[bidder]
    if bit_amount > highest_bid :
        highest_bid = bit_amount
        winner = bidder

print(winner)