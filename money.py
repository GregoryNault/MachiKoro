import cards


def check_roll(dice, player):
    if dice == 1 and player.cards["wheat field"] > 0:
        payment = cards.deck[1][-1] * player.cards["wheat field"]
        print(f"you just got paid {payment} coins by the wheat field")
        player.coins += payment
    if dice == 2 and player.cards["ranch"] > 0:
        payment = cards.deck[2][-1] * player.cards["ranch"]
        print(f"you just got paid {payment} coins by the ranch")
        player.coins += payment
    if dice == 2 or dice == 3 and player.cards["bakery"] > 0:
        payment = cards.deck[23][-1] * player.cards["bakery"]
        print(f"you just got paid {payment} coins by the bakery")
        player.coins += payment
    if dice == 3 and player.cards["cafe"] > 0:
        payment = cards.deck[3][-1] * player.cards["cafe"]
        print(f"you just got paid {payment} coins by the cafe")
        player.coins += payment
    if dice == 4 and player.cards["convenience store"] > 0:
        payment = cards.deck[4][-1] * player.cards["convenience store"]
        print(f"you just got paid {payment} coins by the convenience store")
        player.coins += payment
    if dice == 5 and player.cards["forest"] > 0:
        payment = cards.deck[5][-1] * player.cards["forest"]
        print(f"you just got paid {payment} coins by the forest")
        player.coins += payment
    if dice == 6 and player.cards["stadium"] > 0:
        payment = cards.deck[61][-1] * player.cards["stadium"]
        print(f"you just got paid {payment} coins by the stadium")
        player.coins += payment


def check_coins():
    pass


def make_payment():
    pass