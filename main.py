# Machi Koro game
import random, player, money
import cards


def player_entry():
    # Takes in the number of players, and creates a list of all of their names.
    num_players = input("How many players are there [1-4]: ")
    if num_players.isdigit():
        num_players = int(num_players)
        if 1 <= num_players <= 4:
            player_names = [input("Enter Player Name: ") for i in range(num_players)]
        else:
            print("That is not a correct number of players to add, please try again")
            player_entry()
        # Creates a list of player objects, each player is given a name from the player_names list.
        player_objects_list = [player.Player(player_names[i]) for i in range(num_players)]
        return player_objects_list
    elif num_players.isalnum() or num_players.isalpha():
        print("That is the wrong number of players. Please enter a number between 1 and 4.")
        player_entry()


def roll_dice(player):
    # Rolls two dice, only one is used unless the train station is owned.
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    if player.landmarks["train station"] and player.landmarks["amusement park"] and dice_1 == dice_2:
        # Adding 20 identifies that the player will get another turn because of his amusement park.
        return dice_1 + dice_2 + 20
    if player.landmarks["train station"]:
        return dice_1 + dice_2
    return dice_1


def player_prompt(player):
    # Player action selection menu.
    prompt = input("\nWhat would you like to do?\n[1) Show Coins, 2) Show Cards, 3) Buy Development "
                   "4) Buy Landmark, 5) Show the current deck 6) Pass Turn]: ")
    if prompt == "1":
        print(f"You have {player.coins} coins")
        player_prompt(player)
    elif prompt == "6":
        pass
    elif prompt == "3":
        buy_card = input("Which development card would you like to purchase [For example, 'wheat field']?: ").lower()
        buy_card = player.buy_card(buy_card)
        if not buy_card:
            player_prompt(player)
    elif prompt == "2":
        player.show_cards()
        player_prompt(player)
    elif prompt == "4":
        landmark_list = [key for key in player.landmarks if not player.landmarks[key]]
        landmark = input(f"Which landmark card would you like to purchase [{landmark_list}]?: ").lower()
        player.buy_landmark(landmark)
    elif prompt == "5":
        cards.current_deck()
        player_prompt(player)
    else:
        print("That is not a valid entry, please try again")
        player_prompt(player)
    return False


def player_turn(player, player_list):
    # Extra turn will become true if 20 is added to the dice roll when returned from the dice_roll function.
    global extra_turn
    extra_turn = False

    print(f"Hi {player.name}, it is your turn.")

    # Following lines handle the player dice rolls.
    roll = roll_dice(player)

    if roll > 20:
        print("\nYou have just rolled doubles, you get an extra turn because of your amusement park")
        extra_turn = True
        roll -= 20
    print(f"You have just rolled a {roll}.")

    if player.landmarks["radio tower"]:
        # If radio tower is owned the player may re-roll the dice.
        re_roll_prompt = input("You have a radio tower do you wish to re-roll (y/n)?: ")
        if re_roll_prompt == "y":
            roll = roll_dice(player)
            if roll > 20:
                print("\nYou have just rolled doubles, you get an extra turn because of your amusement park")
                extra_turn = True
                roll -= 20
            print(f"You have just rolled a {roll}.")

    # Checks if dice roll matches player cards and receive coins for any activated cards.
    money.check_roll(roll, player, player_list)

    if player.coins == 0 and player.landmarks["town hall"]:
        player.coins += 1
        print("You had 0 coins, you were give 1 coin by your town hall")

    # Prompts the player to take an action.
    player_prompt(player)

    # Turn finishes checks if player is allowed an extra turn.
    if extra_turn:
        extra_turn = False
        player_turn(player, player_list)


endgame = False
winning_player = None

# Welcome statement and players are created.
print("\nWelcome to Machi Koro!!\n")
player_objects = player_entry()

# Game loop.
while not endgame:
    # Loops through each player.
    for player in player_objects:
        # Deals the three draw piles and goes through player actions.
        cards.current_deck()
        player_turn(player, player_objects)

        # Checks if the user has all 5 landmarks, if so they are the winner.
        if player.landmarks["train station"] and player.landmarks["amusement park"] and \
                player.landmarks["shopping mall"] and player.landmarks["radio tower"]:
            endgame = True
            print(f"Thanks for playing {player.name} won by completing all his city's landmarks!! Congratulations!!")
            break