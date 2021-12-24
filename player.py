class Player:
    def __init__(self):
        self.coins = 3
        self.cards = {
            "wheat field": 1,
            "bakery": 1
        }
        self.landmarks = {
            "Town Hall": True,
            "Amusement Park": False,
            "Shopping Mall": False,
            "Radio Tower": False,
            "Train Station": False
        }
