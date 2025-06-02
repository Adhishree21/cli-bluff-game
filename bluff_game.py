import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        suits = ['♤', '♧', '♡', '♢']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = [Card(s, r) for s in suits for r in ranks]
        random.shuffle(self.cards)

    def deal(self, num_players):
        return [self.cards[i::num_players] for i in range(num_players)]

class Player:
    def __init__(self, name, cards):
        self.name = name
        self.hand = cards

    def show_hand(self):
        return [f"{c.rank}{c.suit}" for c in self.hand]

def display_hand(player):
    """Show cards in hand with index"""
    print(f"\n{player.name}'s Hand:")
    for i, card in enumerate(player.hand):
        print(f"{i+1}: {card.rank}{card.suit}")

def declare_rank(current_rank=None):
    """Ask player to declare a rank (could be a bluff)"""
    if current_rank:
        print(f"Current rank being played: {current_rank}")
        choice = input("Do you want to (p)lay or (pass)? ").strip().lower()
        if choice == 'pass' or choice == 'p':
            return 'PASS'
        else:
            return current_rank
    else:
        declared = input("Declare the rank you're playing (e.g. 5, J, A): ").strip().upper()
        return declared

def select_cards_to_play(player):
    """Ask player to select card indexes from hand to play"""
    display_hand(player)
    indexes = input("Select card positions to play (comma-separated, e.g. 1,3): ").split(",")
    selected = []
    for i in indexes:
        try:
            idx = int(i.strip()) - 1
            if 0 <= idx < len(player.hand):
                selected.append(player.hand[idx])
            else:
                print("Invalid index:", i)
        except ValueError:
            print("Not a number:", i)
    
    # Remove selected cards from hand
    for card in selected:
        player.hand.remove(card)
    return selected

def ask_challenge(next_player):
    """Ask the next player if they want to challenge"""
    while True:
        choice = input(f"\n{next_player.name}, do you want to challenge? (yes / no): ").strip().lower()
        if choice in ['yes', 'no']:
            return choice == 'yes'
        print("Invalid input. Please type 'yes' or 'no'.")

def check_bluff(played_cards, declared_rank):
    """Return True if bluff was detected (i.e. any card doesn't match declared rank)"""
    for card in played_cards:
        if card.rank != declared_rank:
            return True
    return False

def resolve_challenge(current_player, challenger, played_cards, declared_rank, pile):
    """Handle the result of the challenge"""
    print(f"\n🃏 Revealing the cards...")
    print(f"Cards {current_player.name} actually played: {[str(card) for card in played_cards]}")
    
    bluff = check_bluff(played_cards, declared_rank)
    if bluff:
        print(f"\n❌ BLUFF DETECTED! {current_player.name} was lying about having '{declared_rank}'!")
        all_cards = pile + played_cards
        current_player.hand.extend(all_cards)
        print(f"{current_player.name} takes {len(all_cards)} cards from the pile!")
        print(f"{current_player.name} now has {len(current_player.hand)} cards.")
    else:
        print(f"\n✅ NO BLUFF! {current_player.name} was telling the truth!")
        print(f"{challenger.name} wrongly challenged and must take the pile!")
        all_cards = pile + played_cards
        challenger.hand.extend(all_cards)
        print(f"{challenger.name} takes {len(all_cards)} cards from the pile!")
        print(f"{challenger.name} now has {len(challenger.hand)} cards.")

def check_winner(players):
    """Returns the player who has no cards left, or None"""
    for player in players:
        if not player.hand:
            return player
    return None

def play_game():
    print("🂡 Welcome to CLI Bluff! 🂡")
    print("Goal: Be the first to get rid of all your cards!")
    print("You can bluff about the rank of cards you play.")
    print("Other players can challenge you if they think you're lying.\n")
    
    # Get number of players
    while True:
        try:
            num_players = int(input("Enter number of players (2-6): "))
            if 2 <= num_players <= 6:
                break
            else:
                print("Please enter a number between 2 and 6.")
        except ValueError:
            print("Please enter a valid number.")
    
    deck = Deck()
    hands = deck.deal(num_players)
    players = [Player(f"Player {i+1}", hand) for i, hand in enumerate(hands)]
    pile = []  # center pile where cards go
    current_rank = None  # Track the current rank being played
    consecutive_passes = 0  # Track how many players passed in a row

    # Show initial hand sizes
    for player in players:
        print(f"{player.name}: {len(player.hand)} cards")
    
    input("\nPress Enter to start the game...")

    turn = 0
    while True:
        current = players[turn % num_players]
        next_player = players[(turn + 1) % num_players]

        print(f"\n{'='*60}")
        print(f"{current.name}'s Turn")
        print(f"Cards in center pile: {len(pile)}")
        if pile:
            print(f"Last cards played: {len(pile)} cards (face down)")
        if current_rank:
            print(f"Current rank: {current_rank}")
        else:
            print("No current rank - you can play any rank!")
        
        # Show all players' hand sizes
        print(f"\nAll players' hand sizes:")
        for i, player in enumerate(players):
            marker = " <- CURRENT TURN" if player == current else ""
            print(f"  {player.name}: {len(player.hand)} cards{marker}")
        
        print(f"\nYour hand size: {len(current.hand)} cards")
        
        # Show current player's hand
        print(f"\n{current.name}'s Hand:")
        hand_by_rank = {}
        for card in current.hand:
            if card.rank not in hand_by_rank:
                hand_by_rank[card.rank] = []
            hand_by_rank[card.rank].append(card)
        
        for rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
            if rank in hand_by_rank:
                cards = hand_by_rank[rank]
                suits = [card.suit for card in cards]
                print(f"  {rank}: {len(cards)} cards {suits}")

        declared_rank = declare_rank(current_rank)
        
        if declared_rank == 'PASS':
            print(f"{current.name} passes.")
            consecutive_passes += 1
            
            # If everyone passes, reset the rank
            if consecutive_passes >= num_players:
                print(f"\nEveryone passed! Starting new round - you can play any rank now.")
                current_rank = None
                consecutive_passes = 0
            
            turn += 1
            continue
        
        # Reset consecutive passes when someone plays
        consecutive_passes = 0
        current_rank = declared_rank
        
        played_cards = select_cards_to_play(current)

        if not played_cards:
            print("No cards selected. Please try again.")
            continue

        print(f"\n{current.name} claims to have played {len(played_cards)} card(s) of rank '{declared_rank}'")
        print(f"Center pile will have: {len(pile) + len(played_cards)} cards total")

        if ask_challenge(next_player):
            print(f"\n🔍 {next_player.name} challenges {current.name}!")
            resolve_challenge(current, next_player, played_cards, declared_rank, pile)
            pile = []  # pile gets collected by loser
            current_rank = None  # Reset rank after challenge
            consecutive_passes = 0
        else:
            print(f"✅ {next_player.name} accepts the claim.")
            pile += played_cards  # cards added to pile face-down

        winner = check_winner(players)
        if winner:
            print(f"\n🎉 {winner.name} wins the game! 🎉")
            print("Final standings:")
            for player in sorted(players, key=lambda p: len(p.hand)):
                print(f"  {player.name}: {len(player.hand)} cards remaining")
            break

        input("\nPress Enter to continue to next turn...")
        turn += 1

# Main entry point
if __name__ == "__main__":
    play_game()