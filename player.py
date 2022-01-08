import cards


class Player:
    def __init__(self, name):
        self.coins = 30
        self.cards = {
            "wheat field": 1,
            "ranch": 0,
            "bakery": 1,
            "cafe": 0,
            "convenience store": 0,
            "forest": 1,
            "stadium": 0,
            "business center": 0,
            "tv station": 0,
            "cheese factory": 0,
            "furniture factory": 1,
            "mine": 0,
            "family restaurant": 0,
            "apple orchard": 0,
            "fruit market": 0
        }

        self.landmarks = {
            "town hall": True,
            "train station": False,
            "shopping mall": False,
            "amusement park": False,
            "radio tower": False
        }
        self.name = name

    def buy_card(self, card):
        cost = cards.find_cost(card)
        if card in self.cards:
            if self.coins >= cost:
                if cards.check_deck(card):
                    self.coins -= cost
                    self.cards[card] += 1
                    print(f"You have just bought a {card}. You have {self.coins} coins left.")
                    return True
                else:
                    print("That card is not in the deck.")
                    return False
            else:
                print("You don't have enough coins to buy that card.")
                return False
        else:
            print("That card doesn't exist in this game.")
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
                print(f"You have just bought a {card} landmark. You have {self.coins} coins left.")
            else:
                print("You already own that card")
        else:
            print("That landmark does not exits")

    def show_cards(self):
        card_list = []
        for item in self.cards:
            a = (item, self.cards[item])
            card_list.append(a)
        print("\nCards in your hand [(card name, number of cards)]")
        print("*" * 140)
        print(card_list[0:6])
        print(card_list[9:15])
        print(card_list[6:9])
        landmark_list = []
        for item in self.landmarks:
            if self.landmarks[item]:
                landmark_active = 1
            else:
                landmark_active = 0
            landmark = (item, landmark_active)
            landmark_list.append(landmark)
        print(landmark_list)
        print("*" * 140)



