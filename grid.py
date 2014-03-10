import random, time, pygame, sys, copy, numpy, os
from pygame.locals import *
from time import sleep


class Board:

  def __init__(self, rows=8, columns=8, board_layout=None):
    ''' Creating a new Board instance with no arguments
        creates an 16x16 array of zeroes.
        Alternatively, you can create a specific board layout by inputting
        a Numpy array.

        A dead cell is denoted by a 0;
        a live cell is denoted by a 1.
    '''
    if board_layout == None:
      self.board = numpy.zeros(shape=(rows, columns), dtype=numpy.int)
    else:
      print board_layout
      self.board = board_layout
    self.rows = rows
    self.columns = columns
    self.board_transposed = self.board.transpose()
    self.board_flipped = numpy.fliplr(self.board)

  def printboard(self):
    ''' print board layout '''
    print self.board

  def count_adjacent_cells(self, x, y):
    ''' dy = -1, dx = -1, 0, 1
        dy =  0, dx = -1, 0, 1
        dy =  1, dx = -1, 0, 1 '''
    c = 0
    for dy in range(-1, 2):
      if (dy + y) < 0 or (dy + y) > (self.rows - 1):
        c = c + 0
      else:
        for dx in range(-1, 2):
          if (dx + x) < 0 or (dx + x) > (self.columns - 1):
            c = c + 0
          elif (dx == 0) and (dy == 0):
            c = c + 0
          else:
            if self.board[x+dx][y+dy] == 1:
              #print (x+dx, y+dy, self.board[x][y])
              c = c + 1
    #print (x, y, c)
    return c

  def check_action_required(self, x, y):
    '''
    Any live cell with fewer than two live neighbours dies, as if caused by under-population.
    Any live cell with two or three live neighbours lives on to the next generation.
    Any live cell with more than three live neighbours dies, as if by overcrowding.
    Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
    '''
    c = self.count_adjacent_cells(x, y)

    if self.board[x][y] == 0 and c == 3:
      return 1
    if self.board[x][y] == 1 and c < 2:
      return 0
    if self.board[x][y] == 1 and (c == 2 or c == 3):
      return 1
    if self.board[x][y] == 1 and (c > 3):
      return 0
    else:
      return 0


def generate_new_board(board):
  new_board_instance = Board()
  for x in range(0, board.rows):
    for y in range(0, board.columns):
      new_board_instance.board[x][y] = board.check_action_required(x, y)
  return new_board_instance


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
XMARGIN = 4
YMARGIN = 4

EMPTY_SPACE = -1 # an arbitrary, nonpositive value


def main():
    global FPSCLOCK, DISPLAYSURF, GEMIMAGES, GAMESOUNDS, BASICFONT, BOARDRECTS, whiteCell, blackCell
    # Initial set up.

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Life')
    BASICFONT = pygame.font.Font('freesansbold.ttf', 36)

    blackCell = pygame.image.load('img/black.png')
    whiteCell = pygame.image.load('img/white.png')
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

    gameBoard = getBlankBoard()
    DISPLAYSURF.fill(RED)

    while True:
        drawBoard(gameBoard)


def getBlankBoard():
    # Create and return a blank board data structure.
    board = []

    for x in range(BOARDWIDTH):
        board.append([EMPTY_SPACE] * BOARDHEIGHT)

    return board


def drawBoard(board):
    for x in xrange(BOARDWIDTH):
        for y in xrange(BOARDHEIGHT):
            DISPLAYSURF.fill(GRIDCOLOR, BOARDRECTS[x][y])
            pygame.draw.rect(DISPLAYSURF, BLACK, BOARDRECTS[x][y], 1)
            #gemToDraw = board[x][y]
            #if gemToDraw != EMPTY_SPACE:
            DISPLAYSURF.blit(whiteCell, BOARDRECTS[1][1])

    pygame.display.update()


if __name__ == '__main__':
    main()
