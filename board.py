'''
DO NOT CHANGE THIS FILE!

CSC 201
Programming Project 4--AcesUpBoard class

The AcesUpBoard class places cards onto the board and manages the movement
of the cards for the Aces Up Solitaire game. The board has four tableau piles,
one stock pile, and one foundation pile. A play from the stock pile places
one card at the top of each tableau pile. The top card from the tableau can
be moved to the foundation pile, but only if there is another top card in
another tableau pile with the same suit and a higher rank. The top card
from a tableau pile can also be moved to an empty tableau pile. 

'''
from graphics2 import *
from card import *
from deck import *

class AcesUpBoard:
    
    NUM_TABLEAUS = 4
    STOCK_X = 500
    STOCK_Y = 75
    FOUNDATION_X = 500
    FOUNDATION_Y = 200
    INITIAL_TABLEAU_X = 60
    INITIAL_TABLEAU_Y = 75
    HORZ_TO_NEXT_TABLEAU = 90
    VERTICAL_TO_NEXT_CARD = 25
    
    def __init__(self, window):
        '''
        Initializes the four tableaus, the stock pile, and the foundation pile
        in the graphics window
        
        Params:
        window (GraphWin): the window where the four tableaus, the stock pile
        and the foundation pile are drawn
        '''
        self.tableau = [[],[],[],[]]
        
        self.stock = Deck()
        
        stockSpot = Card('cards/0e.gif')
        stockSpot.move(AcesUpBoard.STOCK_X, AcesUpBoard.STOCK_Y)
        stockSpot.draw(window)      
        
        self.stockCard = Card('cards/0b.gif')
        self.stockCard.move(AcesUpBoard.STOCK_X, AcesUpBoard.STOCK_Y)
        self.stockCard.draw(window)
        
        self.emptyList = []
        for i in range(AcesUpBoard.NUM_TABLEAUS):
            card = Card('cards/0e.gif')
            card.move(AcesUpBoard.INITIAL_TABLEAU_X + AcesUpBoard.HORZ_TO_NEXT_TABLEAU * i,
                      AcesUpBoard.INITIAL_TABLEAU_Y)
            self.emptyList.append(card)
            card.draw(window)
        
        foundationSpot = Card('cards/0e.gif')
        foundationSpot.move(AcesUpBoard.FOUNDATION_X, AcesUpBoard.FOUNDATION_Y)
        foundationSpot.draw(window)
        
        self.foundationHidden = True
        self.foundationCard = Card('cards/0b.gif')
        self.foundationCard.move(AcesUpBoard.FOUNDATION_X, AcesUpBoard.FOUNDATION_Y)  
        
    def dealFromStock(self, window):
        '''
        Deals four cards from the stock pile, one to the top of each tableau
        
        Params:
        window (GraphWin): the window where the four tableaus, the stock pile
        and the foundation pile are drawn
        '''
        if not self.stock.isEmpty():
            for i in range(AcesUpBoard.NUM_TABLEAUS):
                card = self.stock.dealCard()
                numCards = len(self.tableau[i])
                card.move(AcesUpBoard.INITIAL_TABLEAU_X + AcesUpBoard.HORZ_TO_NEXT_TABLEAU * i,
                          AcesUpBoard.INITIAL_TABLEAU_Y + numCards * AcesUpBoard.VERTICAL_TO_NEXT_CARD)
                self.tableau[i].append(card)
                card.draw(window)
            if self.stock.isEmpty():
                self.stockCard.undraw()
        
            
    def isEligibleToMoveToFoundation(self, card):
        '''
        Determines in the card received is eligible to be moved to the foundation pile
        meaning the card is the same suit and of lower rank than some other top
        card in a tableau
        
        Params:
        card (Card): the card whose elgibility to be moved will be determines
        
        Returns:
        True if the card is eligible to move to the foundation and false otherwise

        '''
        for column in self.tableau:
            if len(column) > 0 and column[-1].getSuit() == card.getSuit() and column[-1].getRank() > card.getRank():
                return True;
        return False;
    
    def moveCardToFoundation(self, card, window):
        '''
        Moves the card received to the foundation pile. Note: the card must be have
        been determined eligible to be moved before using this method.
        
        Params:
        card (Card): the card to be moved to the foundation pile
        window (GraphWin): the window where the four tableaus, the stock pile
        and the foundation pile are drawn
        
        Returns:
        True if the card is eligible to move to the foundation and false otherwise

        '''
        for column in self.tableau:
            if len(column) > 0 and column[-1] == card:
                column.remove(card)
        card.undraw()
        if self.foundationHidden:
            self.foundationCard.draw(window)
            self.foundationHidden = False
              
       
    def isPointInTopTableauCard(self,point):
        '''
        Checks to see if the point received is in a card at the top of some tableau
        
        Params:
        point (Point)--the point whose location is in question
        
        Returns:
        True if the point is in a card at the top of some tableau, False if not.
        '''
        for column in self.tableau:
            if len(column) > 0 and column[-1].containsPoint(point):
                return True                   
        return False
    
    def isPointInEmptyTableau(self, point):
        '''
        Checks to see if the point received is in an empty tableau
        
        Params:
        point (Point)--the point whose location is in question
        
        Returns:
        True if the point is in an empty tableau, False if not.
        '''
        for i in range(AcesUpBoard.NUM_TABLEAUS):
            if len(self.tableau[i]) == 0 and self.emptyList[i].containsPoint(point):
                return True
        return False
    
    def moveCardToEmptyTableau(self, card, point, window):
        '''
        Moves the card received to the empty tableau determined by the point received.
        Note: The card must be have been determined eligible to be moved and the point
        determined to be in an empty tableau before using this method. The method also
        returns 1 or 0 depending on whether an ace that was not already at the base
        of the tableau has been moved to the base of an empty tableau
        
        Params:
        card (Card): the card to be moved to the empty tableau
        point (Point): the point which is in an empty tableau
        window (GraphWin): the window where the four tableaus, the stock pile
        and the foundation pile are drawn
        
        Returns:
        1 if the card moved to the empty tableau earned a point for the move.
        O if the card moved to the empty tableau does not earn a point for the move.
        '''
        
        for i in range(AcesUpBoard.NUM_TABLEAUS):
            if self.emptyList[i].containsPoint(point):
                emptyX = self.emptyList[i].getImage().getAnchor().getX()
                emptyY = self.emptyList[i].getImage().getAnchor().getY()
                cardX = card.getImage().getAnchor().getX()
                cardY = card.getImage().getAnchor().getY()
                for column in self.tableau:
                    if len(column) > 0 and column[-1] == card:
                        column.remove(card)
                card.undraw()
                card.move(emptyX - cardX, emptyY - cardY)
                self.tableau[i].append(card)
                card.draw(window)
        if card.getRank() == Deck.ACE_HIGH and emptyY != cardY:
            return 1
        else:
            return 0
    
    def isPointInFoundationCard(self, point):
        '''
        Checks to see if the point received is in the foundation
        
        Params:
        point (Point)--the point whose location is in question
        
        Returns:
        True if the point is in the foundation, False if not.
        '''
        return self.foundationCard.containsPoint(point)
     
     
    def isPointInStockCard(self, point):
        '''
        Checks to see if the point received is in the stock pile
        
        Params:
        point (Point)--the point whose location is in question
        
        Returns:
        True if the point is in the stock pile, False if not.
        '''
        return self.stockCard.containsPoint(point)
    
    
    def isStockEmpty(self):
        '''
        Determines if the stock pile is empty or not
        
        Returns:
        True if the stock pile has no cards left; False otherwise
        '''
        return self.stock.getNumCardsLeft() == 0
    
    
    def getCardAtPoint(self, point):
        '''
        checks to see if the point is in some card on the board
        
        Params:
        point (Point)--the point whose location is in question
        
        Returns:
        If the point is in a card on the board, the card is returned.
        If the point is not in any card on the board, None is returned.
        '''
        for column in self.tableau:
            if len(column) > 0 and column[-1].containsPoint(point):
                return column[-1]
        return None
    
    
    def isWin(self):
        '''
        Determines if the board is in a winning state which is one card
        in each tableau and that card is an ace
        
        Returns:
        True if the board is in a winning state; Otherwise return false;
        '''
        for column in self.tableau:
            if len(column) != 1 or column[-1].getRank() != Deck.ACE_HIGH:
                return False
        return True
