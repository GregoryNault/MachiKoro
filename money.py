import cards


def check_roll(dice, player):
    if dice == 1 and player.cards["wheat field"] > 0:
        payment = cards.deck[1][-1] * player.cards["wheat field"]
        print("you just got paid {payment} coins")
        player.coins += payment


def check_coins():
    pass


def make_payment():
    pass