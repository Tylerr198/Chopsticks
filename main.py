# Coding the game chopsticks


#losing condition
# getting both hands out aka. both hands at 5
# not being able to attack or move
# not having any fingers up

#rules of the game
# when transferring, have to have a different combination of hands. so if 2-1, cant do 1-2. it's the same thing


# |||| ||||

# |||| ||||

class Hand():
    def __init__(self):
        self.left = 4
        self.right = 4

    def __repr__(self) -> str:
        return "☝️ " * self.left + " |" + "☝️ " *self.right
    
class Player():
    def __init__(self,):
        self.game_hand = Hand()

    def __repr__(self):
        return repr(self.game_hand)
    

player1 = Player()
player2 = Player()

game_board = "Player 1: " + repr(player1) + "\n-----------------------------" + "\nPlayer 2: " + repr(player2)
print("")
print(game_board)
def start_game():
    pass


    