from random import shuffle

DECKS = 'H S D C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:

    def __init__(self):
        print("Creating a Deck: ")
        self.all_cards = [(s, r) for s in DECKS for r in RANKS]

    def shuffle(self):
        print("Shuffling the Cards: ")
        shuffle(self.all_cards)

    def split_in_half(self):
        return self.all_cards[:26], self.all_cards[26:]


class Hand:

    def __init__(self,cards):
        self.cards = cards

    def __str__(self):
        return "Contains {} cards".format(len(self.cards))

    def add(self,added_cards):
        self.cards.extend(added_cards)

    def remove_card(self):
        return self.cards.pop()

class Player:

    def __init__(self, name, hand):
        self.name = name
        self.hand = hand


    def play_cards(self):
        drawn_card = self.hand.remove_card()
        print("{} has placed {} ".format(self.name,drawn_card))
        print("\n")
        return drawn_card

    def remove_war_cards(self):
        war = []
        if len(self.hand.cards)<3:
            return self.hand.cards
        else:
            for i in range(3):
                war.append(self.hand.remove_card())
            return war

    def still_has_cards(self):
        return len(self.hand.cards) !=0



print("Welcome to the game Let the Battle Begin: ")
print("\n")

d = Deck()
d.shuffle()
half1, half2 = d.split_in_half()

comp = Player("Computer", Hand(half1))

name = input("Enter Your Name: ")
user = Player("Human", Hand(half2))

total_rounds = 0
wars = 0

while user.still_has_cards() and comp.still_has_cards():
    total_rounds += 1
    print("Time for round {}".format(total_rounds))
    print("\n")
    print("Here are the current standings {} has {} and {} has {}".format(user.name,len(user.hand.cards),comp.name,len(comp.hand.cards)))
    print("\n")
    table_cards = []

    print("Playing a card: ")
    print("\n")

    c_card = comp.play_cards()
    p_card = user.play_cards()

    table_cards.append(c_card)
    table_cards.append(p_card)

    if c_card[1] == p_card[1]:
        wars+=1
        print("WarTime! ")
        table_cards.extend(user.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())
        print("\n")
        print("The user's card is: " + str(p_card[0]) + str(p_card[1]))
        print("\n")
        print("The user's card is: " + str(c_card[0]) +" "+ str(c_card[1]))
        print("\n")
        if RANKS.index(p_card[1])>RANKS.index(c_card[1]):
            user.hand.add(table_cards)
            print("User wins this round! ")
        else:
            comp.hand.add(table_cards)
            print("Computer wins this round! ")
    else:
        if RANKS.index(p_card[1])>RANKS.index(c_card[1]):
            user.hand.add(table_cards)
            print("User wins this round! ")
        else:
            comp.hand.add(table_cards)
            print("Computer wins this round! ")


print("\n")

print("Game Over: number of rounds = "+str(total_rounds))

print("\n")

print("Number of Wars: "+str(wars))

print("\n")

if comp.still_has_cards():
    print("Computer Won: ")
else:
    print("User Won: ")


