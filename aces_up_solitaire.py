'''
Name: Abdul
CSC 201
Programming Project 4

The game of Aces Up Solitaire have four tableaus, a stock pile, and
a foundation pile. The object of the game it to move all of the cards
is the deck to the foundation pile except the four aces with will be
the only cards left in the tableaus, one in each tableau. Only the top
card of each tableau pile can be moved to the foundation and only when
the top card of some other tableau is the same suit and a larger rank.
If a tableau has no cards, then the top card of another tableau can be
moved to the empty tableau. If no move can be made then a card can
be dealt from the stock pile to each tableau. One point is earned when
a card is moved to the foundation or an ace is moved to an empty tableau.

This program manages the game by interacting with the AcesUpBoard class.

Document Assistance (who and what or declare no assistance):
Prof Mueller helped me with the loops in the setUpGame and playGame function.
She also helped make my conditional statements work well in the playGame function.
'''

from board import *
from button import *
from deck import *
import time

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 500

def setUpGame():
    '''
    Creates the window with a start button, the tableaus, the stock pile, the
    foundation, and the label for scoring an Aces Up solitaire game. When the
    start button is clicked one card is dealt to each tableau and the button
    is renamed Quit.
    
    Returns:
    the window where the game will be played, the board managing the cards,
    the button now labeled Quit, and the scoring label.
    '''
    window = GraphWin("Aces Up Solitaire", WINDOW_WIDTH, WINDOW_HEIGHT)


    button = Button(Point(506, 450), 60, 30, "Start")
    button.activate()
    button.draw(window)

    scoreLabel = Text(Point(50, 450), "Score: 0")
    scoreLabel.setSize(12)
    scoreLabel.draw(window)

    board = AcesUpBoard(window)  # Create an instance of the AcesUpBoard class

    # Deal one card to each tableau when the start button is clicked
    clickPoint = window.getMouse()
    while not button.isClicked(clickPoint):
        clickPoint = window.getMouse()

    button.setLabel("Quit")

    board.dealFromStock(window)
            

    return window, board, button, scoreLabel


def playGame(window, board, button, scoreLabel):
    '''
    Plays the Aces Up solitaire game enforcing the rules and
    accumulating points as the game progresses.

    Params:
    window (GraphWin): the window where the game is played
    board (AcesUpBoard): the board managing the cards
    button (Button): the button to click to end the game
    scoreLabel (Text): the label showing the game score as the game progresses
    '''
    score = 0
    
    clickPoint = window.getMouse()
    # Main game loop
    while not button.isClicked(clickPoint):
        

        # Check if the stock pile is clicked
        if board.isPointInStockCard(clickPoint):
            board.dealFromStock(window)

        # Check if a tableau card is clicked
        clickedCard = board.getCardAtPoint(clickPoint)
        if clickedCard is not None:
            clickPoint = window.getMouse()
            if board.isEligibleToMoveToFoundation(clickedCard):
                
                if board.isPointInFoundationCard(clickPoint):
                    
                    board.moveCardToFoundation(clickedCard, window)
                    score += 1
                    scoreLabel.setText("Score: " + str(score))
            elif board.isPointInEmptyTableau(clickPoint):
                score += board.moveCardToEmptyTableau(clickedCard, clickPoint, window)
                scoreLabel.setText("Score: " + str(score))

        # Check if the button is clicked
        
        clickPoint = window.getMouse()

 
   
    
def flashingResultDisplay(window, result):
    '''
    Provides text flashing Winner! or Loser :( depending on the text received
    
    Params:
    window (GraphWin): the window where the text will be displayed
    result (String): the text that will be flashed in the window
    '''
    resultText = Text(Point(int(WINDOW_WIDTH / 2), WINDOW_HEIGHT - 50), result)
    resultText.setSize(32)
    resultText.setTextColor('red')
    resultText.draw(window)
    for i in range(20):
        if i % 2 == 0:
            resultText.undraw()
        else:
            resultText.draw(window)
        time.sleep(.2)
    
def main():
    '''
    Sets up the game board, plays the game, and displays where the game
    was won or lost.
    '''
    window, board, button, scoreLabel = setUpGame()
    
    playGame(window, board, button, scoreLabel)
    
    if board.isWin() and board.isStockEmpty():
        result = 'Winner!'
    else:
        result = 'Loser :('
    flashingResultDisplay(window, result)
        
    time.sleep(2)    
    window.close()

if __name__ == '__main__':
    main()
