# Card game
# CARD CLASS
# Suit , rank, value

import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + " of " + self.suit
        
class Deck:
    
    # Deck is a List of (card)objects of class Card 
    # Generating a deck of cards using for loop and global variables suits & ranks and Card Class

    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)
                
                
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    
    def deal_one(self):
        return self.all_cards.pop()

# Player Class
class Player:
    
    # Play from the top and add to the bottom 
    
    # .extend merges two list into a single list , .append creates a nested list if we are adding data of type list
    
    def __init__(self,name):
        self.name = name
        self.all_cards = []
        
    def remove_one(self):
        return self.all_cards.pop(0)
    
    def add_card(self,new_card):
        if type(new_card) == type([]):
            self.all_cards.extend(new_card)
        else:
            self.all_cards.append(new_card)
            
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'

player_one = Player("One")
player_two = Player("Two")

# Setting Game Split the Deck between players
new_deck = Deck()        
new_deck.shuffle()  

# Splitting the deck to the players

for x in range(26):
    player_one.add_card(new_deck.deal_one())
    player_two.add_card(new_deck.deal_one())  

# Game Logic

game_on = True
round_num = 0

while game_on:
    
    round_num += 1
    print(f'Round {round_num}.')
    
    # Check to see if a player is out of cards:
    if len(player_one.all_cards) == 0:
        print("Player One out of cards! Game Over")
        print("Player Two Wins!")
        game_on = False
        break
        
    if len(player_two.all_cards) == 0:
        print("Player Two out of cards! Game Over")
        print("Player One Wins!")
        game_on = False
        break
        
    # New round 
    
    player_one_cards = []   # player one cards held in hand 
    player_one_cards.append(player_one.remove_one())
    
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())
    
    at_war = True
    while at_war:
        
        if player_one_cards[-1].value > player_two_cards[-1].value:
            # Player One gets the cards
            player_one.add_card(player_one_cards)
            player_one.add_card(player_two_cards)
            at_war = False
        
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            # Player One gets the cards
            player_two.add_card(player_one_cards)
            player_two.add_card(player_two_cards)           
            at_war = False

        else:
            print("WAR!!")
        # First check to see if player has enough cards
           
            if len(player_one.all_cards) < 5:
                print("Player One unable to play war! Game Over at War")
                print("Player Two Wins! Player One Loses!")
                game_on = False
                break
            
            elif len(player_two.all_cards) < 5:
                print("Player Two unable to play war! Game Over at War")
                print("Player One Wins! Player One Loses!")
                game_on = False
                break
                
            else:
                # Otherwise, we're still at war, so we'll add the next cards 5 cards as per some random rule set
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())    
            
    