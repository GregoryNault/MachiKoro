import cards


def check_roll(dice, player, player_objects):
    if dice == 1 and player.cards["wheat field"] > 0:
        payment = cards.deck[1][-1] * player.cards["wheat field"]
        player.coins += payment
        print(f"you just got paid {payment} coins by the wheat field. Total coins: {player.coins}")

        for other_player in player_objects:
            if other_player != player:
                other_player_payment = cards.deck[1][-1] * other_player.cards["wheat field"]
                other_player.coins += other_player_payment
                print(f"{other_player.name} just got paid {other_player_payment} for their wheat fields. Total coins: "
                      f"{other_player.coins}")

    if dice == 2 and player.cards["ranch"] > 0:
        payment = cards.deck[2][-1] * player.cards["ranch"]
        player.coins += payment
        print(f"you just got paid {payment} coins by the ranch. Total coins: {player.coins}")

        for other_player in player_objects:
            if other_player != player:
                other_player_payment = cards.deck[1][-1] * other_player.cards["wheat field"]
                other_player.coins += other_player_payment
                print(f"{other_player.name} just got paid {other_player_payment} for their wheat fields. Total coins: "
                      f"{other_player.coins}")

    if dice == 3:
        for other_player in player_objects:
            if other_player.cards["cafe"] > 0 and player.coins > 0:
                payment = other_player.cards["cafe"]
                player.coins -= payment
                other_player.coins += payment
                print(f"You have paid {other_player.name} a total of {payment} coins because of their"
                      f" cafe(s).")

    if dice == 2 or dice == 3 and player.cards["bakery"] > 0:
        payment = cards.deck[23][-1] * player.cards["bakery"]
        player.coins += payment
        print(f"you just got paid {payment} coins by the bakery. Total coins: {player.coins}")

    if dice == 4 and player.cards["convenience store"] > 0:
        payment = cards.deck[4][-1] * player.cards["convenience store"]
        player.coins += payment
        print(f"you just got paid {payment} coins by the ranch. Total coins: {player.coins}")

    if dice == 5 and player.cards["forest"] > 0:
        payment = cards.deck[5][-1] * player.cards["forest"]
        player.coins += payment
        print(f"You just got paid {payment} coins by the ranch. Total coins: {player.coins}")

        for other_player in player_objects:
            other_player_payment = cards.deck[5][-1] * other_player.cards["forest"]
            other_player.coins += other_player_payment
            print(f"{other_player.name} just got paid {other_player_payment} for their forest. Total coins: "
                  f"{other_player.coins}")

    if dice == 6 and player.cards["stadium"] > 0:
        for other_player in player_objects:
            if other_player.coins > 2:
                other_player.coins -= 2
                player.coins += 2
                print(f"You have received 2 coin from {other_player}")
            elif other_player.coins == 1:
                other_player.coins -= 1
                player.coins += 1
                print(f"You have received 1 coin from {other_player}")



