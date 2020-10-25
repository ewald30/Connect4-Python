from unittest import TestCase
from domain1 import*
from AI import *

class TestAI(TestCase):

    def test_player_is_winning(self):
        c = colors
        s = symbols(c)
        b1 = Board()
        b1[0] = 1
        b1[1] = 1
        b1[2] = 1
        p1 = PrettyPrintedBoard(b1,s)
        poz = b1.getline
        ai = AI(b1)
        ai.playerMoves(2,5)
        self.assertEqual(True,ai.playerIsWinning())

