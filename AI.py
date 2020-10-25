import random
from checkWinAlgo import*
import domain1

class AI:
    def __init__(self, board):
        self._board = board
        self._active = False
        self._col = 0
        self._line = 0
        self._move = 0
        self._AIline = 0

    def playerMoves(self, value1, value2):
        self._col = value1
        self._line = value2

    def playerIsWinning(self):
        boardCopy = self._board
        if HorizontalCheck(boardCopy, 1, self._line, 3):
            while boardCopy[self._line,self._col] == -1:
                self._col += 1
                if self._col == 7:
                    break
            right = self._col
            self._col -= 1

            while boardCopy[self._line,self._col] == -1:
                self._col -= 1
            left = self._col

            for i in range(0,7):
                if self._board[self._line,i] == -1:
                    self._board.setSpecificItem(self._line,i,1)

            if right <= 6 and self._board[self._line,right] == 0:
                self._move = right
            elif left >= 0  and self._board[self._line,left] == 0:
                self._move = left

            self._move += 1
        elif VerticalCheck(boardCopy, 1, self._col, 3):
            for i in range(0,6):
                if self._board[i,self._col] == -1:
                    self._board.setSpecificItem(i,self._col,1)
            self._move = self._col+1
        else:
            self._move = random.randint(1,7)

    def aiIsWinning(self):
        boardCopy = self._board
        col = self._move-1
        print(col)
        if VerticalCheck(boardCopy, 2, col, 3):
            for i in range(0,6):
                if self._board[i,self._col] == -1:
                    self._board.setSpecificItem(i,self._col,1)
            self._move = self._col+1
            print(self._move)
        else:
            self._move = random.randint(1,7)

        #if DiagonalCheckLR(board1, 1, self._line, self._col, 3):
        #if DiagonalCheckRL(board1, 1, self._line, self._col, 3):



    @property
    def Active(self):
        return self._active

    def Activate(self):
        self._active = True


    @property
    def get_move(self):
        return self._move