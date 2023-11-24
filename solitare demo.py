from board import *
from button import *
from deck import *
import time

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 500


def setUpGame():
    window = GraphWin("Aces Up Solitaire", WINDOW_WIDTH, WINDOW_HEIGHT)
    window.setCoords(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)

    button = Button(Point(50, 20), 60, 30, "Start")
    button.activate()

    scoreLabel = Text(Point(WINDOW_WIDTH - 50, 20), "Score: 0")
    scoreLabel.setSize(12)
    scoreLabel.draw(window)

    board = AcesUpBoard(window)  # Create an instance of the AcesUpBoard class

    # Draw the tableaus
    for i in range(AcesUpBoard.NUM_TABLEAUS):
        tableauX = AcesUpBoard.INITIAL_TABLEAU_X + AcesUpBoard.HORZ_TO_NEXT_TABLEAU * i
        tableauY = AcesUpBoard.INITIAL_TABLEAU_Y
        emptyTableauCard = board.emptyList[i]
        emptyTableauCard.move(tableauX, tableauY)
        emptyTableauCard.draw(window)

    # Draw the stock pile
    stockSpot = Card('cards/0e.gif')
    stockSpot.move(AcesUpBoard.STOCK_X, AcesUpBoard.STOCK_Y)
    stockSpot.draw(window)

    stockCard = board.stockCard
    stockCard.move(AcesUpBoard.STOCK_X, AcesUpBoard.STOCK_Y)
    stockCard.draw(window)

    # Draw the foundation
    foundationSpot = Card('cards/0e.gif')
    foundationSpot.move(AcesUpBoard.FOUNDATION_X, AcesUpBoard.FOUNDATION_Y)
    foundationSpot.draw(window)

    # Deal one card to each tableau when the start button is clicked
    while True:
        clickPoint = window.getMouse()
        if button.clicked(clickPoint):
            button.setLabel("Quit")
            button.deactivate()
            board.dealFromStock(window)
            break

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
    

    # Main game loop
    while True:
        clickPoint = window.getMouse()

        # Check if the stock pile is clicked
        if board.isPointInStockCard(clickPoint):
            board.dealFromStock(window)

        # Check if a tableau card is clicked
        clickedTableau = board.getCardAtPoint(clickPoint)
        if clickedTableau is not None:
            if board.isEligibleToMoveToFoundation(clickedTableau):
                board.moveCardToFoundation(clickedTableau, window)
                score += 1
                scoreLabel.setText("Score: " + str(score))
            elif board.isPointInEmptyTableau(clickPoint):
                score += board.moveCardToEmptyTableau(clickedTableau, clickPoint, window)
                scoreLabel.setText("Score: " + str(score))

        # Check if the button is clicked
        if isWithinBounds(clickPoint, button):
            break

    # Update the score and check if the game is won
    scoreLabel.setText("Score: " + str(score))
    if board.isWin():
        flashingResultDisplay(window, "Winner!")
    else:
        flashingResultDisplay(window, "Loser :(")
        
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