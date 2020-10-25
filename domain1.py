class colors:
    blue = '\033[94m'
    green = '\033[92m'
    white = '\033[39m'
    red = '\033[91m'


class symbols:
    '''
    Class for symbols used in the board
        * white empty square  - empty
        * blue filled square  - player1's dot
        * green filled square - player2's dot
    '''
    def __init__(self, colors):
        self._colors = colors
        self._empty = chr(0x25a1)
        self._player1 = self._colors.blue+chr(0x25a0)+self._colors.white
        self._player2 = self._colors.green+chr(0x25a0)+self._colors.white
        self._won = self._colors.red+chr(0x25a0)+self._colors.white

    @property
    def Won(self):
        return self._won

    @property
    def Player1(self):
        return self._player1

    @property
    def Player2(self):
        return self._player2

    @property
    def Empty(self):
        return self._empty


class Board:
    '''
    Used when working with the board
    '''
    def __init__(self):
        self._board = []
        self._line = 0
        self._iter = 0
        for i in range(0,6):
            row = [0]*7
            self._board.append(row)

    @property
    def copy(self):
        return self._board.copy()

    @property
    def getline(self):
        return self._line

    @property
    def iterations(self):
        return self._iter

    def setSpecificItem(self,x,y,value):
        self._board[x][y] = value

    def clear(self):
        self._line = 0
        self._iter = 0
        board = []
        for i in range(0,6):
            row = [0]*7
            board.append(row)
        self._board = board

    def __getitem__(self, tup):
        x,y = tup
        return self._board[x][y]

    def __setitem__(self, x, value):
        if x < 0 or x >6:
            raise Exception('Invalid Position!!!')
        for i in range(5,-1,-1):
            if self._board[i][x] == 0:
                self._board[i][x] = value
                self._line = i
                self._iter += 1
                return


class PrettyPrintedBoard():
    '''
    Used when printing the board
    '''
    def __init__(self, board, symbols):
        self._board = board
        self._symbols = symbols

    def __str__(self):
        mat = '\n\n'
        chr = ''
        line = '                             1 2 3 4 5 6 7\n'
        mat = mat + line
        for i in range(0, 6):
            line ='                             '
            for j in range(0, 7):
                chr = ''
                if self._board[i,j] == 0:
                    chr += self._symbols.Empty
                elif self._board[i,j] == 1:
                    chr += self._symbols.Player1
                elif self._board[i,j] == 2:
                    chr += self._symbols.Player2
                elif self._board[i,j] == -1:
                    chr += self._symbols.Won
                line = line + chr + ' '
            line = line + '\n'
            mat = mat+line
        return mat

