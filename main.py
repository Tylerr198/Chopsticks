class Hand():
    def __init__(self):
        self.left = 1
        self.right = 1

    def __repr__(self) -> str:
        if self.left <= 0 or self.left >= 5:
            left_hand = " DEAD"
            self.left = 0  # Reset value
        else:
            left_hand = "☝️ " * self.left

        if self.right <= 0 or self.right >= 5:
            right_hand = " DEAD"
            self.right = 0  # Reset value
        else:
            right_hand = "☝️ " * self.right
        return left_hand + " | " + right_hand
    
class Player():
    def __init__(self, name):
        self.name = name
        self.game_hand = Hand()

    def __repr__(self) -> str:
        return self.name
    
    def show_hand(self) -> str:
        return repr(self.game_hand)
    
    # Method for transferring points between hands
    def transfer(self) -> None:
        while True:
            print("Hand to transfer points to")
            direction = direction_input()
            amount = amount_input()
            if direction == "l": # Transfer to left hand
                temp = self.game_hand.left + amount
                if self.game_hand.right == temp:
                    print("\nInvalid move. Please choose again. Will result in same combo")
                    continue
                temp = self.game_hand.right
                if self.game_hand.right < amount or amount <= 0:
                    print("\nInvalid move. Please choose again\n")
                    continue
                self.game_hand.left += amount
                self.game_hand.right -= amount
                break
            elif direction == "r": # Transfer to right hand
                temp = self.game_hand.right + amount
                if self.game_hand.left == temp:
                    print("\nInvalid move. Please choose again. Will result in same combo")
                    continue
                if self.game_hand.left < amount or amount <= 0:
                    print("\nInvalid move. Please choose again\n")
                    continue
                self.game_hand.right += amount
                self.game_hand.left -= amount
                break
            print("\nSuccessful transfer")
            break

    def update_hand(self, side: str, amount:int) -> None:
        if side == "l":
            self.game_hand.left += amount
        else:
            self.game_hand.right += amount
    

# Function for "attacking" opponent hand
def hit(attacker: Player, opp: Player) -> bool:
    while True:
        # Get hand direction for attacking and attacked
        print("\nYour hand to attack with")
        attack_hand_str = direction_input()
        attack_hand_pt = attacker.game_hand.left if attack_hand_str == "l" else attacker.game_hand.right
        if attack_hand_pt == 0: # Case: Attacking with dead hand
            print("\nThat hand is dead. You can't attack with it")
            continue

        print("\nOpponent hand to attack")
        opp_hand_str = direction_input()
        opp_hand_pt = opp.game_hand.left if opp_hand_str == "l" else opp.game_hand.right
        if opp_hand_pt == 0: # Case: Attacking a dead hand
            print("\nThat hand is dead. You can't attack it")
            continue
 
        if attack_hand_pt + opp_hand_pt > 5: # Case: Attacking a hand brings it over 5 points
            print("\nYou can't hit that hand. It would go over 5 points")
        else:
            opp.update_hand(opp_hand_str, attack_hand_pt)
            print("\nSuccessful attack")
            break

def show_board(player1: Player, player2: Player) -> None:
    print(f"{player1}: " + player1.show_hand() + "\n-----------------------------" + f"\n{player2}: " + player2.show_hand())

def player_choices(player1: Player, player2: Player) -> None:
    print(f"\n{player1}'s Move")
    move_choice = hit_trasnfer_input()
    if move_choice == "t":
        player1.transfer()
    if move_choice == "h":
        hit(player1, player2)


# Check state of game to determine if there is a winner
def check_winner(player1: Player, player2: Player) -> bool:
    if player1.game_hand.left == 0 and player1.game_hand.right == 0:
        print(f"\n{player2} is the winner!!")
        return True
    elif player2.game_hand.left == 0 and player2.game_hand.right == 0:
        print(f"\n{player1} is the winner!!")
        return True
    return False    

# Helper functions to validate inputs
def direction_input() -> str:
    while True:
        direction = input("Left or right(l/r): ")
        if direction != "l" and direction != "r":
            print("Choose l or r")
        else:
            break
    return direction

def hit_trasnfer_input() -> str:
    while True:
        move_choice = input("hit or transfer (h/t): ")
        if move_choice != "h" and move_choice != "t":
            print("Choose h or t")
        else:
            break
    return move_choice

def amount_input()-> str:
    while True:
        amount = input("Amount: ")
        try:
            amount = int(amount)
            break
        except ValueError:
            print("Please enter a number")
    return amount

def start_game() -> None:
    # initialize game
    player1 = Player("Player 1")
    player2 = Player("Player 2")
    turn_count = 0
    print("")
    show_board(player1, player2)

    # game loop
    while True:
        if turn_count % 2 == 0:
            player_choices(player1, player2)
        else:
            player_choices(player2, player1)
        print("\nCurrent Board\n---------------------------")
        show_board(player1, player2)
        is_winner = check_winner(player1, player2)
        turn_count += 1
        if is_winner:
            return

if __name__ == "__main__":
    start_game()




    