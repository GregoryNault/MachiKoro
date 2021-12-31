import cards


class Player:
    def __init__(self, name):
        self.coins = 3
        self.cards = {
            "wheat field": 1,
            "ranch": 0,
            "bakery": 1,
            "cafe": 0,
            "convenience store": 0,
            "forest": 0,
            "stadium": 0
        }
        self.landmarks = {
            "town hall": True,  #True,
            "amusement park": True,  #False,
            "shopping mall": True, #False,
            "radio tower": True, #False,
            "train station": False
        }
        self.name = name

    def buy_card(self, card):
        cost = cards.find_cost(card)
        if card in self.cards:
            if cards.check_deck(card):
                if self.coins >= cost:
                    self.coins -= cost
                    self.cards[card] += 1

                    if card in cards.dealt_cards1:
                        cards.dealt_cards1.remove(card)
                    elif card in cards.dealt_cards2:
                        cards.dealt_cards2.remove(card)
                    elif card in cards.dealt_cards3:
                        cards.dealt_cards3.remove(card)

                    print(f"You have just bought a {card}. You have {self.coins} coins left.")
                    return True
                else:
                    print("You don't have enough coins")
                    return False
            else:
                print("That card is not in the deck")
                return False


        else:
            print("that card doesn't exist")
            return False

    def buy_landmark(self, card):
        cost = cards.find_cost(card)
        if card in self.landmarks:
            if not self.landmarks[card]:
                if self.coins >= cost:
                    self.coins -= cost
                else:
                    print("you don't have enough money for that card")
                    return
                self.landmarks[card] = True
            else:
                print("You already own that card")
        else:
            print("that card is not valid")

    def check_landmarks(self, card):
        for item in self.landmarks:
            if not self.landmarks[item]:
                return False
            else:
                return True
