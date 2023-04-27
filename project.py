
#importing dependencies
import random as rd

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


print(logo)


# Define the deck of cards and their values
deck = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5,
        '6': 6, '7': 7, '8': 8, '9': 9, 'J': 10, 'Q': 10, 'K': 10}

# Define the player's and dealer's hands as empty lists
player_hand = []
dealer_hand = []

# Define a function to deal cards to a hand
def deal_card(hand):
    card = rd.choice(list(deck.keys()))
    hand.append(card)

# Deal two cards to the player and two cards to the dealer
for i in range(2):
    deal_card(player_hand)
    deal_card(dealer_hand)

# Show the player's hand and one of the dealer's cards
print(f"Player's Hand: {player_hand}")
print(f"Dealer's Hand: [{dealer_hand[0]}, *]")

# Define a function to calculate the value of a hand
def calculate_hand_value(hand):
    # Calculate the sum of the card values
    value = sum([deck[card] for card in hand])
    # Check if the hand contains an Ace (value 1 or 11)
    if 'A' in hand and value <= 11:
        value += 10
    return value

# Define a function to check if a hand has busted (value over 21)
def has_busted(hand):
    return calculate_hand_value(hand) > 21

# Define a function to play the dealer's turn
def play_dealer_turn(hand):
    while calculate_hand_value(hand) < 17:
        deal_card(hand)

# Ask the player if they want to hit or stand
while True:
    choice = input("Do you want to hit or stand? ")
    if choice.lower() == 'hit':
        deal_card(player_hand)
        print(f"Player's Hand: {player_hand}")
        if has_busted(player_hand):
            print("Player has busted. Dealer wins!")
            break
    elif choice.lower() == 'stand':
        # Play the dealer's turn
        play_dealer_turn(dealer_hand)
        print(f"Dealer's Hand: {dealer_hand}")
        # Determine the winner
        if has_busted(dealer_hand):
            print("Dealer has busted. Player wins!")
        elif calculate_hand_value(player_hand) > calculate_hand_value(dealer_hand):
            print("Player wins!")
        elif calculate_hand_value(player_hand) < calculate_hand_value(dealer_hand):
            print("Dealer wins!")
        else:
            print("It's a tie!")
        break
