# Machi Koro game
import random, player, money
import cards


def roll_dice(player):
    dice_1 = random.randint(1, 6)
    if player.landmarks["Train Station"]:
        dice_2 = random.randint(1, 6)
        return dice_1 + dice_2
    return dice_1


def player_turn(player):
    # Player rolls a dice (2 dice if they own a train station)
    roll = roll_dice(player)
    print(f"You have just rolled a {roll}")

    # Checks if dice roll matches player cards and receive coins for any activated cards.
    money.check_roll(roll, player)


endgame = False
greg = player.Player()
cards.create_draw_piles()

while not endgame:
    player_turn(greg)
    if input("what do you want to do") == "coins":
        print(greg.coins)
    elif "pass":
        pass





