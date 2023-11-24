'''
Name: Abdul
CSC 201
Programming Project 4--Deck Class

The Deck class represents a stadard deck of playing cards with or without two jokers.
The card files for the graphic of each card are in a folder named cards. Each card
file is named with its rank and a letter for its suit. For example, the 4 of hearts
is in the file 4h.gif while the jack of clubs is in  the file 11c.gif.

Document Assistance (who and what or declare no assistance):



'''
from card import Card
import random

class Deck:
    ACE_HIGH = 14
    ACE_LOW = 1
    

    def __init__(self, aces_high=True, use_jokers=False):
        '''
        

        Params:
        aces_high (bool): Indicates whether aces will be high in the game
        (ie. rank 14, True) or low (ie. rank 1, False).
        
        use_jokers(bool): Indicates whether two jokers will be used in the deck in
        addition to the standard 52 cards in a poker deck (ie 52 cards, False) 
        
        '''
        self.cardList = []  
        self.currentIndex = 0  
        suits = ['c', 'd', 'h', 's']  
        
        if aces_high:
            rankRange = range(2, 15)
        else:
            rankRange = range(1, 14)
        # loop through all ranks and suits when aces are high
        for rank in rankRange:
            for suit in suits:
                file_name = "cards/{}{}.gif".format(rank, suit)
                self.cardList.append(Card(file_name))
        # loops for aces low
       
        if use_jokers:
            self.cardList.append(Card('cards/0j.gif'))
            self.cardList.append(Card('cards/0j.gif'))
        
        
        self.shuffle()
    
    def getFullDeckSize(self):
        '''returns the number of number of cards in this deck '''
        return len(self.cardList) 

    
    def shuffle(self):
        '''
        shuffles the cards in the list and sets the current index to zero
        '''
        random.shuffle(self.cardList)  
        self.currentIndex = 0  # reset current index to 0
    
    def dealCard(self):
        '''
        return: returns the card at the current index and increments
        the current index so that next time dealCard is called,
        the next card is returned
        '''
        card = self.cardList[self.currentIndex]  
        self.currentIndex += 1  
        return card
    
    def isEmpty(self):
        '''
        returns True if all of the cards have been dealt and False if not
        '''
        return self.currentIndex == len(self.cardList)  
    
    def getNumCardsLeft(self):
        '''
        returns the number of cards that have not yet been dealt
        '''
        return len(self.cardList) - self.currentIndex  
    
    def __str__(self):
        '''
        returns a string with each card in the deck on one line
        '''
        result = ""
        for card in self.cardList:
            result += str(card) + "\n"  
        return result
    
    
    
# Test code for the Deck class.
def main():
    deck = Deck()
    print('Print entire shuffled deck.')
    print(deck)
    print('Full deck size:', deck.getFullDeckSize())
    
    print('\nDeal 5 cards')
    for i in range(5):
        card = deck.dealCard()
        print(card)
    
    print('\nNum cards left to deal:', deck.getNumCardsLeft())
    print('Is deck empty?', deck.isEmpty());
    
    print('\nDeal remaining cards without printing them.')
    for i in range(47):
        card = deck.dealCard()
    
    print('\nNum cards left to deal:', deck.getNumCardsLeft())
    print('Is deck empty?', deck.isEmpty());
    print()
    
    print('\nReshuffle the cards and print again.')
    deck.shuffle()
    print(deck)
    
    deck2 = Deck(False)
    print('\nCreate a new deck with aces low, no Jokers, and print it.')
    print(deck2)
    print('Full deck size:', deck2.getFullDeckSize())
    
    deck3 = Deck(True, True)
    print('\nCreate a new deck with aces high with Jokers and print it.')
    print(deck3)
    print('Full deck size:', deck3.getFullDeckSize())
    
    
    deck4 = Deck(False, True)
    print('\nCreate a new deck with aces low with Jokers and print it.')
    print(deck4)
    print('Full deck size:', deck4.getFullDeckSize())
        
    
main()
        