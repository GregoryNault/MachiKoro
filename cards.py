import random

# These are all the development cards in the deck and also the player landmark cards.
# [name, cards in hand, cost, player payout]
deck = {
    1: ["wheat field", 116, 1, 1],
    2: ["ranch", 116, 1, 1],
    23: ["bakery", 116, 1, 1],
    3: ["cafe", 116, 2, 1],
    4: ["convenience store", 116, 2, 3],
    5: ["forest", 116, 3, 1],
    61: ["stadium", 116, 6, 2],
    62: ["business center", 116, 8, 0],
    63: ["tv station", 116, 7, 5],
    7: ["cheese factory", 116, 5, 3],
    8: ["furniture factory", 116, 3, 3],
    9: ["mine", 116, 6, 5],
    910: ["family restaurant", 116, 3, 2],
    10: ["apple orchard", 116, 3, 3],
    1112: ["fruit market", 116, 2, 2],
    "L1": ["train station", 0, 4],
    "L2": ["shopping mall", 0, 10],
    "L3": ["amusement park", 0, 16],
    "L4": ["radio tower", 0, 22]
}

# When dealt the cards are divided and dealt out in three separate piles.
# Cards that activate between 1-5, establishment cards 6, cards between 7 and 12.
dealt_cards1 = []
dealt_cards2 = []
dealt_cards3 = []


def create_draw_piles():
    # Creates a four card pile from cards that activate on a roll between 1 and 5.
    card_names = [(deck[key][0], deck[key][2]) for key in deck if deck[key][1] > 0]
    while len(dealt_cards1) < 4:
        dealt_card = card_names[random.randint(0, 5)]
        dealt_cards1.append(dealt_card)
        for key in deck:
            # This removes the cards that are placed into the pile from the deck.
            if deck[key][0] == dealt_card[0]:
                deck[key][1] -= 1
    print(dealt_cards1)

    # Creates a 2 card pile from the establishment cards (activate on a roll of 6).
    while len(dealt_cards2) < 2:
        dealt_card = card_names[random.randint(6, 8)]
        dealt_cards2.append(dealt_card)
        for key in deck:
            if deck[key][0] == dealt_card[0]:
                deck[key][1] -= 1
    print(dealt_cards2)

    # Creates a 4 card pile from cards that activate on a roll between 7 and 12.
    while len(dealt_cards3) < 4:
        dealt_card = card_names[random.randint(9, 14)]
        dealt_cards3.append(dealt_card)
        for key in deck:
            if deck[key][0] == dealt_card[0]:
                deck[key][1] -= 1
    print(dealt_cards3)


def find_cost(card):
    # Returns the cost of the card.
    for key in deck:
        if deck[key][0] == card:
            return deck[key][2]


def check_deck(card):
    # When a player buys a card it checks if the card is in one of the three dealt piles and removes it if it is.
    for i in range(len(dealt_cards1)):
        if dealt_cards1[i][0] == card:
            dealt_cards1.pop(i)
            return True
    for i in range(len(dealt_cards2)):
        if dealt_cards2[i][0] == card:
            dealt_cards2.pop(i)
            return True
    for i in range(len(dealt_cards3)):
        if dealt_cards3[i][0] == card:
            dealt_cards3.pop(i)
            return True


def current_deck():
    # Prints out the cards that currently dealt out for all users.
    print("\nCurrent Deck (card name, cost)")
    print("-" * 100)
    create_draw_piles()
    print("-" * 100)
