'''
Name: Abdul
CSC 201
Programming Project 4--Card Class

The Card class represents one standard poker card for a card game. Cards have a rank
and a suit. The card stores its position in a graphics window. It can be drawn and
undrawn in the graphics window.

Document Assistance (who and what or declare no assistance):
Prof Mueller helped me with the containsPoint method.


'''
from graphics2 import *
import time

class Card:
    def __init__(self, fileName):
        '''
        A card image's file name will be received 
        Using that file name, an Image object will be created
        storing it in the instance variable image.
        The instance variables rank and suit also will be initialized.
        
        Params:
        fileName(Text): The filename of the card image
        
        '''
        self.image = Image(Point(0, 0), fileName)
        self.suit = fileName[-5]
        
        
        
        if len(fileName) == 13:
            self.rank = int(fileName[6:8])
        else:
            self.rank = int(fileName[6])
            
        
    
    def getRank(self):
        ''' Returns the rank of the card '''
        return self.rank
    
    def getSuit(self):
        '''Returns the suit of the card'''
        return self.suit
    
    def getImage(self):
        '''Returns the image of the card'''
        return self.image
    
    def draw(self, window):
        '''
        Draws the card in  the window
        
        Params:
        window(GraphWin):The window the card will be drawn.
        '''
        self.image.draw(window)
        
    def undraw(self):
        '''
        Undraws the cards in the window
        
        '''
        self.image.undraw()
        
    def move(self, dx, dy):
        '''
        moves the card dx pixels in the horizontal direction
        and dy pixels in the vertical direction
        
        params:
        dx(int): the x value of the card
        dy(int): the y value of the card

        '''
        self.image.move(dx, dy)
        
    def containsPoint(self, point):
        '''
        Checks of the point is within the bounds of the card
        Params:
        point(Point): The point received

        returns:
        returns True if the point received as a parameter is
        within the bounds of the card. Otherwise, it returns False.
        '''
        self.center = self.image.getAnchor()
        x = point.getX()
        y = point.getY()
        width = self.image.getWidth()
        height = self.image.getHeight()
        
        if (self.center.getX() - width/2) <= x <= (self.center.getX() + width/2) and \
           (self.center.getY() - height/2) <= y <= (self.center.getY() + height/2):
               return True
        else:
               return False

        
    def __str__(self):
         "returns a string/text version of the card suit, rank, and x and y values of the center"
         return "suit = {}, rank = {}, center = {}".format(self.suit, self.rank, self.image.getAnchor())
   

# test code for the Card class
def main():
    
    window = GraphWin("Testing Card", 500, 500)
    
    # create King of Hearts card
    fileName = 'cards/13h.gif'
    card = Card(fileName)

    # print card using __str__ and test getRank, getSuit, getImage
    print(card)
    print(card.getRank())
    print(card.getSuit())
    print(card.getImage())
    
    # move card to center of window and display it
    card.move(250, 250)
    card.draw(window)
    
    # click on card should move it 100 pixels left
    point = window.getMouse()
    while not card.containsPoint(point):
        point = window.getMouse()
    card.move(-100, 0)
    
    # click on card should move it 200 pixels right
    point = window.getMouse()
    while not card.containsPoint(point):
        point = window.getMouse()
    card.move(200, 0)
        
    # print the card using __str__
    print(card)
    
    # stall 2 seconds
    time.sleep(2)
    
    # create 2 of Diamonds card
    fileName = 'cards/2d.gif'
    card2 = Card(fileName)

    # print card2 using __str__ and test getRank, getSuit
    print(card2)
    print(card2.getRank())
    print(card2.getSuit())

    # move card to center of window and display it
    card2.move(250, 250)
    card2.draw(window)
    
    # stall 2 seconds then remove both cards from the window
    time.sleep(2)
    card.undraw()
    card2.undraw()
    
    # stall 2 seconds then close the window
    time.sleep(2)
    window.close()
    
if __name__ == '__main__':
    main()
        
        