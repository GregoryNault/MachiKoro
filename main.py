# Machi Koro game
import random, player, money
import cards

def player_entry():
    num_players = input("How many players are there [1-4]: ")
    if num_players.isdigit():
        num_players = int(num_players)
        if 1 <= num_players <= 4:
            player_names = [input("Enter Player Name: ") for i in range(num_players)]
        else:
            print("That is not a correct number of players to add, please try again")
            player_entry()
        player_objects_list = [player.Player(player_names[i]) for i in range(num_players)]
        return player_objects_list
    elif num_players.isalnum() or num_players.isalpha():
        print("That is the wrong number of players. Please enter a number between 1 and 4.")
        player_entry()


def roll_dice(player):
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    if player.landmarks["train station"] and player.landmarks["amusement park"] and dice_1 == dice_2:
        return dice_1 + dice_2 + 20
    if player.landmarks["train station"]:
        return dice_1 + dice_2
    return dice_1


def player_prompt(player):
    prompt = input("\nWhat would you like to do [coins, show cards, buy card, buy landmark or pass]: ").lower()
    if prompt == "coins":
        print(f"You have {player.coins} coins")
        player_prompt(player)
    elif prompt == "pass":
        pass
    elif prompt == "buy card":
        buy_card = input("which card?: ").lower()
        buy_card = player.buy_card(buy_card)
        if not buy_card:
            player_prompt(player)
    elif prompt == "show cards":
        player.show_cards()
        player_prompt(player)
    elif prompt == "buy landmark":
        landmark_list = [key for key in player.landmarks if not player.landmarks[key]]
        landmark = input(f"which landmark? [{landmark_list}: ").lower()
        player.buy_landmark(landmark)
    else:
        print("That is not a valid entry, please try again")
        player_prompt(player)
    return False


def player_turn(player, player_list):
    # Player rolls a dice (2 dice if they own a train station)
    global extra_turn
    extra_turn = False
    print(f"Hi {player.name}, it is your turn.")
    roll = roll_dice(player)

    if roll > 20:
        print("You have just rolled doubles, you get an extra turn because of your amusement park")
        extra_turn = True
        roll -= 20
    print(f"You have just rolled a {roll}.")

    if player.landmarks["radio tower"]:
        re_roll_prompt = input("You have a radio tower do you wish to re-roll (y/n)?: ")
        if re_roll_prompt == "y":
            roll = roll_dice(player)
            if roll > 20:
                print("You have just rolled doubles, you get an extra turn because of your amusement park")
                extra_turn = True
                roll -= 20
            print(f"You have just rolled a {roll}.")

    # Checks if dice roll matches player cards and receive coins for any activated cards.
    money.check_roll(roll, player, player_list)

    if player.coins == 0 and player.landmarks["town hall"]:
        player.coins += 1
        print("You had 0 coins, you were give 1 coin by your town hall")

    player_prompt(player)

    if extra_turn:
        extra_turn = False
        player_turn(player, player_list)


endgame = False
winning_player = None

print("\nWelcome to Machi Koro!!\n")
player_objects = player_entry()


while not endgame:
    for player in player_objects:
        print("\nCurrent Deck (card name, cost)")
        print("-" * 100)
        cards.create_draw_piles()
        print("-" * 100)
        player_turn(player, player_objects)

        if player.landmarks["train station"] and player.landmarks["amusement park"] and \
                player.landmarks["shopping mall"] and player.landmarks["radio tower"]:
            endgame = True
            print(f"Thanks for playing {player.name} won by completing all his city's landmarks!! Congratulations!!")
            break