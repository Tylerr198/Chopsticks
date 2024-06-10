class Hand():
    def __init__(self):
        self.left = 1
        self.right = 1

    def __repr__(self) -> str:
        left_count = "☝️ " * self.left
        right_count = "☝️ " *self.right
        if self.left <= 0 or self.left == 5:
            self.left = 0
            left_count = " DEAD"
        if self.right <= 0 or self.right == 5:
            self.right = 0
            right_count = " DEAD"
        return left_count + " |" + right_count
    
class Player():
    def __init__(self, name):
        self.name = name
        self.game_hand = Hand()

    def __repr__(self) -> str:
        return self.name
    
    def show_hand(self) -> str:
        return repr(self.game_hand)
    
    # method for transferring points between hands
    def transfer(self, direction: str, amount: int) -> bool:
        if direction == "l":
            if self.game_hand.right < amount:
                return False
            self.game_hand.left += int(amount)
            self.game_hand.right -= int(amount)
        elif direction == "r":
            if self.game_hand.left < amount:
                return False
            self.game_hand.right += int(amount)
            self.game_hand.left -= int(amount)
        return True

    def update_hand(self, side: str, amount:int):
        if side == "l":
            self.game_hand.left += amount
        else:
            self.game_hand.right += amount
    

# function for "attacking" opponent hand
def hit(attacker: Player, opp: Player) -> bool:
    attack_hand_side = direction_input()
    opp_hand_side = direction_input()

    attack_hand = attacker.game_hand.left if attack_hand_side == "l" else attacker.game_hand.right
    opp_hand = opp.game_hand.left if opp_hand_side == "l" else opp.game_hand.right
    if attack_hand + opp_hand > 5:
        print("You can't hit that hand")
        return False
    elif attack_hand == 0:
        print("That hand is dead. You can't attack with it")
        return False
    elif opp_hand == 0:
        print("That hand is dead. You can't attack it")
    else:
        opp.update_hand(opp_hand_side, attack_hand)
        print("Successful attack")
    return True

def show_board(player1, player2):
    print("Player 1: " + player1.show_hand() + "\n-----------------------------" + "\nPlayer 2: " + player2.show_hand())

def transfer_choice():
    return [direction_input(), amount_input()]

def player_choices(player1, player2):
    print(f"\n{player1}'s Choice")
    move_choice = hit_trasnfer_input()
    
    if move_choice == "t":
        choices = transfer_choice()
        transfer_success = player1.transfer(choices[0], choices[1])
        while not transfer_success:
            print("\nInvalid move. Please choose again\n")
            choices = transfer_choice()
            transfer_success = player1.transfer(choices[0], choices[1])
    if move_choice == "h":
        hit_success = hit(player1, player2)
        while not hit_success:
            hit_success = hit(player1, player2)

def check_winner(player1: Player, player2: Player):
    if player1.game_hand.left <= 0 and player1.game_hand.right <= 0:
        print(f"{player2} is the winner!")
        return True
    elif player2.game_hand.left <= 0 and player2.game_hand.right <= 0:
        print(f"{player1} is the winner!")
        return True
    return False
    
def start_game():
    # initialize game
    player1 = Player("player 1")
    player2 = Player("player 2")
    turn_count = 0
    print("")
    show_board(player1, player2)

    # game loop
    while True:
        if turn_count % 2 == 0:
            player_choices(player1, player2)
        else:
            player_choices(player2, player1)
        print("")
        print("Current Board\n---------------------------")
        show_board(player1, player2)
        is_winner = check_winner(player1, player2)
        turn_count += 1
        if is_winner:
            return
        

# Helper functions to validate inputs
def direction_input():
    while True:
        direction = input("Left or right(l/r): ")
        if direction != "l" and direction != "r":
            print("Choose l or r")
        else:
            break
    return direction

def hit_trasnfer_input():
    while True:
        move_choice = input("hit or transfer (h/t): ")
        if move_choice != "h" and move_choice != "t":
            print("Please choose h or t")
        else:
            break
    return move_choice

def amount_input():
    while True:
        amount = input("Amount: ")
        try:
            amount = int(amount)
            break
        except ValueError:
            print("Invalid input. Please enter a number")
    return amount



if __name__ == "__main__":
    start_game()




    