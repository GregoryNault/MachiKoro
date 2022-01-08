import cards


def check_roll(dice, player, player_objects):
    if dice == 1:
        if player.cards["wheat field"] > 0:
            payment = cards.deck[1][-1] * player.cards["wheat field"]
            player.coins += payment
            print(f"You just got paid {payment} coins by your wheat field(s). Total coins: {player.coins}")

        for other_player in player_objects:
            if other_player != player and other_player.cards["wheat field"] > 0:
                other_player_payment = cards.deck[1][-1] * other_player.cards["wheat field"]
                other_player.coins += other_player_payment
                print(f"{other_player.name}, just got paid {other_player_payment} for their wheat fields. Total coins: "
                      f"{other_player.coins}")

    if dice == 2:
        if player.cards["ranch"] > 0:
            payment = cards.deck[2][-1] * player.cards["ranch"]
            player.coins += payment
            print(f"You just got paid {payment} coins by your ranch(es). Total coins: {player.coins}")

        for other_player in player_objects:
            if other_player != player and other_player.cards["ranch"] > 0:
                other_player_payment = cards.deck[1][-1] * other_player.cards["ranch"]
                other_player.coins += other_player_payment
                print(f"{other_player.name}, just got paid {other_player_payment} for their ranch. Total coins: "
                      f"{other_player.coins}")

    if dice == 3:
        for other_player in player_objects:
            if player.coins == 0 and other_player != player:
                print(f"You have no coins to give {other_player.name}.")
            if other_player.cards["cafe"] > 0 and player.coins > 0 and other_player != player:
                payment = other_player.cards["cafe"]
                if other_player.landmarks["shopping mall"]:
                    payment += 1 * other_player.cards["cafe"]
                if payment > player.coins:
                    payment = player.coins
                player.coins -= payment
                other_player.coins += payment
                print(f"You have paid {other_player.name} a total of {payment} coins because of their cafe(s).")

    if dice == 2 or dice == 3 and player.cards["bakery"] > 0:
        payment = cards.deck[23][-1] * player.cards["bakery"]
        if player.landmarks["shopping mall"]:
            mall_payment = 1 * player.cards["bakery"]
            payment += mall_payment
            print(f"Your bakery earned an extra {mall_payment} coins thanks to your shopping mall.")
        player.coins += payment
        print(f"You just got paid {payment} coins by your bakery(s). Total coins: {player.coins}")

    if dice == 4 and player.cards["convenience store"] > 0:
        payment = cards.deck[4][-1] * player.cards["convenience store"]
        if player.landmarks["shopping mall"]:
            mall_payment = 1 * player.cards["convenience store"]
            payment += mall_payment
            print(f"Your convenience store earned an extra {mall_payment} coins thanks to your shopping mall.")
        player.coins += payment
        print(f"You just got paid {payment} coins by your convenience store(s). Total coins: {player.coins}")

    if dice == 5:
        if player.cards["forest"] > 0:
            payment = cards.deck[5][-1] * player.cards["forest"]
            player.coins += payment
            print(f"You just got paid {payment} coins by your forest(s). Total coins: {player.coins}")

        for other_player in player_objects:
            if other_player != player and other_player.cards["forest"]:
                other_player_payment = cards.deck[5][-1] * other_player.cards["forest"]
                other_player.coins += other_player_payment
                print(f"{other_player.name}, just got paid {other_player_payment} for their forest(s). Total coins: "
                      f"{other_player.coins}")

    if dice == 6 and player.cards["stadium"] > 0:
        for other_player in player_objects:
            if other_player != player:
                if other_player.coins > 2:
                    other_player.coins -= 2
                    player.coins += 2
                    print(f"You have received 2 coin from {other_player.name}")
                elif other_player.coins == 1:
                    other_player.coins -= 1
                    player.coins += 1
                    print(f"You have received 1 coin from {other_player.name}")

    if dice == 6 and player.cards["business center"]:
        business_center(player, player_objects)

    if dice == 6 and player.cards["tv station"]:
        player_list = [other_player.name for other_player in player_objects if other_player != player and \
                       other_player.coins > 0]
        if len(player_list) == 0:
            print("There is no one playing that can pay you any money.")
        else:
            select = True
            player_select = ""
            while select:
                player_select = input(f"Which player do you wish to take payment from {player_list}: ")
                if player_select in player_list:
                    break
                else:
                    print("That is not a valid player, please try again.")
            for other_player in player_objects:
                if other_player.name == player_select and other_player != player:
                    if other_player.coins >= 5:
                        other_player.coins -= 5
                        player.coins += 5
                        print(f"{other_player.name} has paid you 5 coins. Total coins: {player.coins}")
                    elif other_player.coins >= 1:
                        print(f"{other_player.name} has paid you {other_player.coins} coins. Total coins: "
                              f"{player.coins}")
                        player.coins += other_player.coins
                        other_player.coins = 0
                    elif other_player.coins == 0:
                        print(f"{other_player.name} doesn't have enough coins to pay you")

    if dice == 7 and player.cards["cheese factory"] > 0:
        payment = cards.deck[7][-1] * player.cards["ranch"] * player.cards["cheese factory"]
        player.coins += payment
        print(f"You just got paid {payment} coins by your cheese factory(s). Total coins: {player.coins}")

    if dice == 8 and player.cards["furniture factory"] > 0:
        payment = cards.deck[8][-1] * (player.cards["forest"] + player.cards["mine"]) * player.cards["furniture " \
                                                                                                     "factory"]
        player.coins += payment
        print(f"You just got paid {payment} coins by your furniture factory(s). Total coins: {player.coins}")

    if dice == 9 or dice == 10:
        for other_player in player_objects:
            if player.coins == 0 and other_player != player:
                print(f"You have no coins to give {other_player.name}")
            if other_player.cards["family restaurant"] > 0 and player.coins > 0 and other_player != player:
                payment = other_player.cards["family restaurant"] * 2
                if other_player.landmarks["shopping mall"]:
                    payment += 1 * other_player.cards["family restaurant"]
                if payment > player.coins:
                    payment = player.coins
                player.coins -= payment
                other_player.coins += payment
                print(f"You have paid {other_player.name} a total of {payment} coins "
                      f"because of their family restaurant(s).")

    if dice == 9:
        if player.cards["mine"] > 0:
            payment = cards.deck[9][-1] * player.cards["mine"]
            player.coins += payment
            print(f"You just got paid {payment} coins by your mine(s). Total coins: {player.coins}")

        for other_player in player_objects:
            if other_player != player and other_player.cards["mine"] > 0:
                other_player_payment = cards.deck[9][-1] * other_player.cards["mine"]
                other_player.coins += other_player_payment
                print(f"{other_player.name}, just got paid {other_player_payment} for their mine(s). Total coins: "
                      f"{other_player.coins}")

    if dice == 10:
        if player.cards["apple orchard"] > 0:
            payment = cards.deck[10][-1] * player.cards["apple orchard"]
            player.coins += payment
            print(f"You just got paid {payment} coins by your apple orchard(s). Total coins: {player.coins}")

        for other_player in player_objects:
            if other_player != player and other_player.cards["apple orchard"] > 0:
                other_player_payment = cards.deck[10][-1] * other_player.cards["apple orchard"]
                other_player.coins += other_player_payment
                print(f"{other_player.name}, just got paid {other_player_payment} for their apple orchard(s). "
                      f"Total coins: {other_player.coins}")

    if dice == 11 and player.cards["fruit market"] > 0 or dice == 12 and player.cards["fruit market"] > 0:
        payment = cards.deck[1112][-1] * (player.cards["wheat field"] + player.cards["apple orchard"]) * \
                  player.cards["fruit market"]
        player.coins += payment
        print(f"You just got paid {payment} coins by your fruit market(s). Total coins: {player.coins}")


def business_center(player, player_objects):
    players = [other_player.name for other_player in player_objects if other_player != player]
    player_to_trade = input(f"Pick another player to trade cards with [{players}]: ")
    if player_to_trade in players:
        for other_player in player_objects:
            if other_player.name == player_to_trade:
                other_player.show_cards()
                pick_other_player_card = business_center_card_selection(other_player, 1)

                while pick_other_player_card is None:
                    print("that is an invalid choice")
                    pick_other_player_card = business_center_card_selection(other_player, 1)

                player.show_cards()
                pick_your_card = business_center_card_selection(player, 0)

                while pick_your_card is None:
                    print("You have picked an invalid choice")
                    pick_your_card = business_center_card_selection(player, 0)

                other_player.cards[pick_your_card] += 1
                player.cards[pick_your_card] -= 1
                player.cards[pick_other_player_card] += 1
                other_player.cards[pick_other_player_card] -= 1
                print(f"You have taken the {pick_other_player_card} from {other_player.name} and given "
                      f"them a {pick_your_card}.")
    else:
        print("That is not a correct player name, please try again.")
        business_center(player, player_objects)


def business_center_card_selection(other_player, other):
    if other == 1:
        selected_card = input(f"Which card do you want to take from {other_player.name}?: ")
    else:
        selected_card = input(f"Pick one of your cards to give to the other player: ")

    # For some reason if you entered a value that wasn't true it would reload the function like it should
    # but when you did enter a valid entry it would return the first invalid one. That is why i put in the while loops
    if selected_card in other_player.cards and other_player.cards[selected_card] > 0:
        return selected_card




