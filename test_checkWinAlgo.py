from unittest import TestCase
from domain1 import*
from checkWinAlgo import *

class Test(TestCase):
    def test_horizontal_check(self):
        b = Board()
        b[3] = 1
        b[4] = 1
        b[5] = 1
        b[6] = 1
        c = colors
        s = symbols(c)
        p = PrettyPrintedBoard(b,s)
        poz = b.getline
        self.assertEqual(True,HorizontalCheck(b,1,poz,4))
        b1 = Board()
        b1[0] = 1
        b1[1] = 1
        b1[2] = 1
        b1[3] = 1
        p1 = PrettyPrintedBoard(b1,s)
        poz = b1.getline
        self.assertEqual(True,HorizontalCheck(b1,1,poz,4))
        b2 = Board()
        b2[0] = 1
        b2[1] = 1
        b2[2] = 1
        b2[6] = 1
        poz = b2.getline
        p2 = PrettyPrintedBoard(b2, s)
        self.assertEqual(False,HorizontalCheck(b2,1,poz,4))



    def test_vertical_check(self):
        b = Board()
        b[2] = 1
        b[2] = 1
        b[2] = 1
        b[2] = 1
        c = colors
        s = symbols(c)
        p = PrettyPrintedBoard(b,s)
        self.assertEqual(True,VerticalCheck(b,1,2,4))
        b1 = Board()
        b1[2] = 2
        b1[2] = 2
        b1[2] = 1
        b1[2] = 1
        b1[2] = 1
        b1[2] = 1
        p1 = PrettyPrintedBoard(b1,s)
        self.assertEqual(True,VerticalCheck(b1,1,2,4))

    def test_diagonal_check_LR(self):
        b = Board()
        b[1] = 1
        b[1] = 1
        b[1] = 1
        b[2] = 2
        b[2] = 1
        b[3] = 1
        b[0] = 1
        b[0] = 1
        b[0] = 2
        b[0] = 1
        c = colors
        s = symbols(c)
        p = PrettyPrintedBoard(b,s)
        poz = b.getline
        DiagonalCheckLR(b,1,poz,0,4)
        b1= Board()
        b1[1] = 1
        b1[2] = 2
        b1[3] = 1
        b1[4] = 2
        b1[2] = 1
        b1[2] = 1
        b1[2] = 1
        b1[3] = 2
        b1[3] = 1
        b1[4] = 1
        b1[1] = 1
        b1[1] = 1
        b1[1] = 2
        b1[1] = 1
        p1 = PrettyPrintedBoard(b1,s)
        poz = b1.getline
        self.assertEqual(True, DiagonalCheckLR(b1,1,poz,1,4))

    def test_diagonal_check_RL(self):
        c = colors
        s = symbols(c)
        b1= Board()
        b1[6] = 1
        b1[3] = 1
        b1[4] = 2
        b1[5] = 1
        b1[5] = 1
        b1[5] = 1
        b1[5] = 2
        b1[3] = 2
        b1[4] = 1
        b1[4] = 2
        b1[6] = 1
        b1[6] = 1
        b1[6] = 2
        b1[6] = 2
        p1 = PrettyPrintedBoard(b1,s)
        poz = b1.getline
        self.assertEqual(DiagonalCheckRL(b1,2,poz,6,4),True)





