import random, time, pygame, sys, copy
from pygame.locals import *
from time import sleep

FPS = 30 # frames per second to update the screen
WINDOWWIDTH = 600  # width of the program's window, in pixels
WINDOWHEIGHT = 600 # height in pixels

BOARDWIDTH = 8 # how many columns in the board
BOARDHEIGHT = 8 # how many rows in the board
SQUARESIZE = 64 # width & height of each space in pixels

PURPLE    = (255,   0, 255)
LIGHTBLUE = (170, 190, 255)
BLUE      = (  0,   0, 255)
RED       = (255, 100, 100)
BLACK     = (  0,   0,   0)
BROWN     = ( 85,  65,   0)

GRIDCOLOR = BLUE # color of the game board


# constants for direction values
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

# The amount of space to the sides of the board to the edge of the window
# is used several times, so calculate it once here and store in variables.
XMARGIN = int((WINDOWWIDTH - SQUARESIZE * BOARDWIDTH) / 2)
YMARGIN = int((WINDOWHEIGHT - SQUARESIZE * BOARDHEIGHT) / 2)

EMPTY_SPACE = -1 # an arbitrary, nonpositive value




def main():
    global FPSCLOCK, DISPLAYSURF, GEMIMAGES, GAMESOUNDS, BASICFONT, BOARDRECTS
    # Initial set up.
    
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Life')
    BASICFONT = pygame.font.Font('freesansbold.ttf', 36)
    # Create pygame.Rect objects for each board space to
    # do board-coordinate-to-pixel-coordinate conversions.
    BOARDRECTS = []
    for x in range(BOARDWIDTH):
        BOARDRECTS.append([])
        for y in range(BOARDHEIGHT):
            r = pygame.Rect((XMARGIN + (x * SQUARESIZE),
                             YMARGIN + (y * SQUARESIZE),
                             SQUARESIZE,
                             SQUARESIZE))
            BOARDRECTS[x].append(r)

    while True:
     DISPLAYSURF.fill(RED)
     runGame()



def runGame():
   

    # initalize the board
    gameBoard = getBlankBoard()
    drawBoard(gameBoard)

def getBlankBoard():
    # Create and return a blank board data structure.
    board = []
    for x in range(BOARDWIDTH):
        board.append([EMPTY_SPACE] * BOARDHEIGHT)
    return board

def drawBoard(board):
    
    for x in range(BOARDWIDTH):
        print x
        for y in range(BOARDHEIGHT):
            print y
            pygame.draw.rect(DISPLAYSURF, GRIDCOLOR, BOARDRECTS[x][y], 1)
            #gemToDraw = board[x][y]
            #if gemToDraw != EMPTY_SPACE:
            #    DISPLAYSURF.blit(GEMIMAGES[gemToDraw], BOARDRECTS[x][y])

if __name__ == '__main__':
    main()
