import cards


def check_roll(dice, player, player_objects):

    # This function takes in the dice roll of the player, the player who's turn it is, and the list of player objects.
    # Used to determine which of the players cards are activated, the payment amount, which players are paid and by who.
    if dice == 1:
        # The wheat field is a community style card - all players in player_objects that own a wheat field are paid.
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
        # The ranch is a community style card - all players in player_objects that own a ranch are paid.
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
        # When the player rolls a 3 the player pays a coin to anyone else that owns one or more cafes.
        # The player's coins cannot go below 0, this card is used first before the bakery.
        # If the player who owns the cafe also owns a shopping mall the current user must pay 1 extra coin per cafe.
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
        # The bakery is a card that only pays the current player if they roll a 2 or 3.
        # If the current player owns a shopping mall landmark then an extra 1 coin per bakery is added.
        payment = cards.deck[23][-1] * player.cards["bakery"]
        if player.landmarks["shopping mall"]:
            mall_payment = 1 * player.cards["bakery"]
            payment += mall_payment
            print(f"Your bakery earned an extra {mall_payment} coins thanks to your shopping mall.")
        player.coins += payment
        print(f"You just got paid {payment} coins by your bakery(s). Total coins: {player.coins}")

    if dice == 4 and player.cards["convenience store"] > 0:
        # The convenience store pays only the current player if they roll a 4.
        # If the current player owns a shopping mall landmark then an extra 1 coin per convenience store is added.
        payment = cards.deck[4][-1] * player.cards["convenience store"]
        if player.landmarks["shopping mall"]:
            mall_payment = 1 * player.cards["convenience store"]
            payment += mall_payment
            print(f"Your convenience store earned an extra {mall_payment} coins thanks to your shopping mall.")
        player.coins += payment
        print(f"You just got paid {payment} coins by your convenience store(s). Total coins: {player.coins}")

    if dice == 5:
        # The mine a community style card - all players in player_objects that own a mine are paid.
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
        # All other players must pay the current player 2 coins when the current player rolls a 6.
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
        # The TV Station is an establishment card - the current player selects another player to take 5 coins from.
        # The player_list is a list of players that have at least 1 coin they can pick from.
        player_list = [other_player.name for other_player in player_objects if other_player != player and \
                       other_player.coins > 0]
        if len(player_list) == 0:
            print("There is no one playing that can pay you any money.")
        else:
            select = True
            player_select = ""
            while select:
                # This continue to loop until a player in the list is selected - invalid entries are ignored.
                player_select = input(f"Which player do you wish to take payment from {player_list}: ")
                if player_select in player_list:
                    break
                else:
                    print("That is not a valid player, please try again.")
            for other_player in player_objects:
                # Goes through the player_objects and finds the object that has a matching name to the name entered.
                # Takes payment from that player and gives it to the current player.
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
        # The Cheese Factory pays the current player 3 coins for every ranch they own.
        payment = cards.deck[7][-1] * player.cards["ranch"] * player.cards["cheese factory"]
        player.coins += payment
        print(f"You just got paid {payment} coins by your cheese factory(s). Total coins: {player.coins}")

    if dice == 8 and player.cards["furniture factory"] > 0:
        # The Furniture Factory pays the current player 3 coins for every forest and mine they own.
        payment = cards.deck[8][-1] * (player.cards["forest"] + player.cards["mine"]) * player.cards["furniture " \
                                                                                                     "factory"]
        player.coins += payment
        print(f"You just got paid {payment} coins by your furniture factory(s). Total coins: {player.coins}")

    if dice == 9 or dice == 10:
        # When the player rolls a 9 or 10 the player pays a coin to anyone else that owns family restaurants.
        # The player's coins cannot go below 0, this card is used first before the mine or the orchard.
        # If the player who owns the restaurant also owns a shopping mall the player must pay 1 extra coin per card.
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
        # The mine is a community style card - all players in player_objects that own a mine are paid 5 coins.
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
        # The apple orchard is a community style card - all players in player_objects that own an orchard are paid.
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
        # The Fruit Market pays the current player 3 coins for every wheat field and apple orchard mine they own.
        payment = cards.deck[1112][-1] * (player.cards["wheat field"] + player.cards["apple orchard"]) * \
                  player.cards["fruit market"]
        player.coins += payment
        print(f"You just got paid {payment} coins by your fruit market(s). Total coins: {player.coins}")


def business_center(player, player_objects):
    # This is called from the check_roll function for when the player rolls a 6 and owns a business center card.
    # A separate function to solve the issue of inputting an incorrect name.

    # Creates a list of the other players names, then asks current player to pick from the list.
    # If input does not match a player from the list the function is called again.
    players = [other_player.name for other_player in player_objects if other_player != player]
    player_to_trade = input(f"Pick another player to trade cards with [{players}]: ")
    if player_to_trade in players:
        for other_player in player_objects:
            # If the input is a correct it finds the correct player object. It shows the others players card.
            if other_player.name == player_to_trade:
                other_player.show_cards()
                # This function handles the selection of the other players cards, the second argument selects which
                # prompt to use in the function (other player vs. current player).
                pick_other_player_card = business_center_card_selection(other_player, 1)

                while pick_other_player_card is None:
                    # If a wrong input is given then the function is called again.
                    print("that is an invalid choice")
                    pick_other_player_card = business_center_card_selection(other_player, 1)

                player.show_cards()
                # same as above except you are picking from the current players cards to trade.
                pick_your_card = business_center_card_selection(player, 0)

                while pick_your_card is None:
                    # If a wrong input is given then the function is called again.
                    print("You have picked an invalid choice")
                    pick_your_card = business_center_card_selection(player, 0)

                # Trades the selected cards between the two players.
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
    # Prompts which cards to trade.
    if other == 1:
        selected_card = input(f"Which card do you want to take from {other_player.name}?: ")
    else:
        selected_card = input(f"Pick one of your cards to give to the other player: ")

    # For some reason if you entered a value that wasn't true it would reload the function like it should
    # but when you did enter a valid entry it would return the first invalid one. That is why i put in the while loops
    if selected_card in other_player.cards and other_player.cards[selected_card] > 0:
        return selected_card




