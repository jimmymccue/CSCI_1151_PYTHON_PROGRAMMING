import random

class Coin:
    """ The coin class contains methods and attributes to interact with coins during play. """

    def __init__(self):
        self.amount = 20
        self.sideup = 'Heads'

    def toss(self):
        rand_side = random.randint(0,1)

        if rand_side == 0:
            self.sideup = 'Heads'
        else:
            self.sideup = 'Tails'

    def get_sideup(self):
        return self.sideup
    
    def get_amount(self):
        return self.amount
    
    def set_amount(self, change):
        self.amount += change


