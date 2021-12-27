class Player:
    def __init__(self):
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
            "Town Hall": True,
            "Amusement Park": False,
            "Shopping Mall": False,
            "Radio Tower": False,
            "Train Station": False
        }

    def buy_card (self, card, cost):
        if self.coins > cost:
            self.coins -= cost
        if card in self.cards:
            self.cards[card][1] += 1
