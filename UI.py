from domain1 import*
from checkWinAlgo import*
from AI import*
from tkinter import*

class UI:
    def __init__(self, board, print_board, name1, name2, colors,ai):
        self._gameover = False
        self._board = board
        self._printb = print_board
        self._name1 = name1
        self._name2 = name2
        self._colors = colors
        self._ai = ai

    def player1WinCheck(self,cmd):
        try:
            cmd = int(cmd)
        except Exception:
            print('                         Invalid Input!')
        cmd -= 1
        self._board[cmd] = 1
        poz = self._board.getline
        self._ai.playerMoves(cmd,poz)
        self._ai.playerIsWinning()
        if HorizontalCheck(self._board, 1, poz,4) or VerticalCheck(self._board, 1, cmd,4) or DiagonalCheckLR(self._board, 1,poz,cmd,4) or DiagonalCheckRL(self._board, 1, poz, cmd,4):
            print('\n\n\n                               ' + self._name1 + ' won!')
            print(self._printb)
            cmd = input('                        Do you want to restart? [y/n]')
            if cmd == 'y':
                self._board.clear()
                self.run()
            else:
                self._gameover = True
                self._turn = 'x'
                return True

    def player2WinCheck(self,cmd):
        try:
            cmd = int(cmd)
        except Exception:
            print('                         Invalid Input!')
        cmd -= 1
        self._board[cmd] = 2
        poz = self._board.getline
        if HorizontalCheck(self._board, 2, poz,4) or VerticalCheck(self._board, 2, cmd,4) or DiagonalCheckLR(self._board, 2, poz,cmd,4) or DiagonalCheckRL( self._board, 2, poz, cmd,4):
            print('\n\n\n                               ' + self._name2 + ' won!')
            print(self._printb)
            cmd = input('                        Do you want to restart? [y/n]')
            if cmd == 'y':
                self._board.clear()
                self.run()
            else:
                self._gameover = True
                self._turn = 'x'
                return True

    def drawCheck(self):
        if IzzaDrawCheck(self._board):
            print('                              Izza ' + self._colors.red + 'Draw' + self._colors.white + '!!!')
            print(self._printb)
            cmd = input('                        Do you want to restart? [y/n]')
            if cmd == 'y':
                self._board.clear()
                self.run()
            else:
                self._gameover = True
                self._turn = 'x'
                return True

    def run(self):
        print('\n\n\n\n\n')
        self._turn = '1'
        print(self._printb)
        while(not self._gameover):
            try:

                if self._turn == '1':
                    if self._ai.Active:
                        self._turn = 'ai'
                    else :self._turn = '2'
                    cmd = input('\n\n\n                   '+self._name1+' enter a number from 1 to 7: ')
                    print('\n\n\n\n\n')
                    if cmd == 'x':
                        break
                    if self.player1WinCheck(cmd):
                        break
                    if self.drawCheck():
                        break
                    print(self._printb)

                if self._turn == '2':
                    self._turn = '1'
                    cmd = input('\n\n\n                   '+self._name2+' enter a number from 1 to 7: ')
                    print('\n\n\n\n\n')
                    if cmd == 'x':
                        break
                    if self.player2WinCheck(cmd):
                        break
                    if self.drawCheck():
                        break
                    print(self._printb)

                if self._turn == 'ai':
                    self._turn = '1'
                    cmd = self._ai.get_move
                    print('\n\n\n\n\n')
                    if self.player2WinCheck(cmd):
                        break
                    if self.drawCheck():
                        break
                    print(self._printb)

            except Exception as e:
                print('                         ',e)




