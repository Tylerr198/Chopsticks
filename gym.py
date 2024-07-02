import gymnasium as gym
from gymnasium import spaces
from main import Player

class Hands(gym.Env):
    metadata = {"render.modes": ["human"]}

    def __init__(self):
        # Initialize players
        self.player1 = Player("Player 1")
        self.player2 = Player("Player 2")
        self.observation_space = [self.player1.game_hand.left, self.player1.game_hand.right, self.player2.game_hand.left, self.player2.game_hand.right]
        
        # Action space: hit, left / right, left /r right
        # Action space: transfer, left / right, amount
        self.action_space = spaces.MultiDiscrete([2,2,2])

    def reset(self):
        # Reset players
        self.player1 = Player("Player 1")
        self.player2 = Player("Player 2")
        return [self.player1.game_hand.left, self.player1.game_hand.right, self.player2.game_hand.left, self.player2.game_hand.right]
    
    def step(self, action):
        pass