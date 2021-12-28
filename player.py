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
            "town hall": True,
            "amusement park": False,
            "shopping mall": False,
            "radio tower": False,
            "train station": False
        }
        self.name = name

    def buy_card(self, card):
        cost = cards.find_cost(card)
        if card in self.cards:
            if self.coins > cost:
                self.coins -= cost
                cards.check_deck(card)
            else:
                print("you don't have enough money for that card")
                return
            self.cards[card] += 1
        else:
            print("that card doesn't exist")
            return

    def buy_landmark(self, card):
        cost = cards.find_cost(card)
        if card in self.landmarks:
            if not self.landmarks[card]:
                if self.coins > cost:
                    self.coins -= cost
                else:
                    print("you don't have enough money for that card")
                    return
                self.landmarks[card] = True
            else:
                print("You already own that card")
        else:
            print("that card is not valid")
