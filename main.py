# Machi Koro game
import random, player, money
import cards


def roll_dice(player):
    dice_1 = random.randint(1, 6)
    if player.landmarks["train station"]:
        dice_2 = random.randint(1, 6)
        return dice_1 + dice_2
    return dice_1


def player_prompt(player):
    prompt = input("what do you want to do [coins, show cards, buy, landmark or pass]: ").lower()
    if prompt == "coins":
        print(player.coins)
        player_prompt(player)
    elif prompt == "pass":
        pass
    elif prompt == "buy":
        buy_card = input("which card?: ").lower()
        buy_card = player.buy_card(buy_card)
        if not buy_card:
            player_prompt(player)
    elif prompt == "show cards":
        print(player.cards)
        print(player.landmarks)
        player_prompt(player)
    elif prompt == "landmark":
        landmark = input("which landmark?: ").lower()
        player.buy_landmark(landmark)
        #if player.check_landmarks(landmark):
            #endgame = True
    else:
        print("That is not a valid entry, please try again")
        player_prompt(player)
    return False


def player_turn(player, player_list):
    # Player rolls a dice (2 dice if they own a train station)
    print(f"hi, welcome to machi koro {player.name}")
    roll = roll_dice(player)
    print(f"You have just rolled a {roll}")

    # Checks if dice roll matches player cards and receive coins for any activated cards.
    money.check_roll(roll, player, player_list)
    player_prompt(player)


endgame = False

num_players = int(input("How many players are there?: "))
player_names = [input("Enter Player Name: ") for i in range(num_players)]

player_objects = [player.Player(player_names[i]) for i in range(num_players)]


while not endgame:
    for player in player_objects:
        cards.create_draw_piles()
        player_turn(player, player_objects)
        for landmark in player.landmarks:
            if player.landmarks[landmark]:
                endgame = True
                winning_player = player
            else:
                endgame = False
        print(endgame)

print(f"The winning player is {winning_player}")





