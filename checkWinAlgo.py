def HorizontalCheck(board,player,x,nb):
    count = 0
    found = False
    poz = 0
    for i in range(0,7):
        if board[x,i] == player:
            count+=1
        else:
            count = 0
        if count == nb:
            poz = i
            found = True
            break
    if found:
        while(board[x,poz] == player):
            board.setSpecificItem(x,poz,-1)
            poz-=1

    return found


def VerticalCheck(board,player,y,nb):
    count = 0
    found = False
    poz = 0
    for i in range(0,6):
        if board[i,y] == player:
            count+=1
        else:
            count = 0
        if count == nb:
            poz = i
            found = True
            break
    if found:
        while(board[poz,y] == player):
            board.setSpecificItem(poz,y,-1)
            poz-=1

    return found

def DiagonalCheckLR(board, player,line,col,nb):

    sline = line
    scol = col
    eline = line
    ecol = col
    found = False

    while sline >0 and scol >0:
        sline -= 1
        scol -= 1

    while eline < 5 and ecol < 6:
        eline += 1
        ecol += 1
    pl = sline
    pr = scol
    count = 0

    while sline <= eline and scol <= ecol:
        if board[sline,scol] == player:
            count += 1
        else:
            count = 0
        sline += 1
        scol += 1
        if count == nb:
            found = True
            pl = sline-1
            pr = scol-1
            break
    if found:
        while board[pl,pr] == player:
            board.setSpecificItem(pl,pr,-1)
            pl -= 1
            pr -= 1

    return found

def DiagonalCheckRL(board, player,line,col,nb):

    sline = line
    scol = col
    eline = line
    ecol = col
    found = False

    while sline > 0 and scol < 6:
        sline -= 1
        scol += 1

    while eline < 5 and ecol > 0:
        eline += 1
        ecol -= 1
    pl = sline
    pr = scol
    count = 0

    while sline <= eline and scol >= ecol:
        if board[sline,scol] == player:
            count += 1
        else:
            count = 0
        sline += 1
        scol -= 1
        if count == nb:
            found = True
            pl = sline-1
            pr = scol+1
            break
    if found:
        while board[pl,pr] == player:
            board.setSpecificItem(pl,pr,-1)
            pl -= 1
            pr += 1
            if pl < 0 or pr >6:
                break
    return found

def IzzaDrawCheck(b):
    if b.iterations == 42:
        for i in range(0,6):
            for j in range(0,7):
                b.setSpecificItem(i,j,-1)
        return True
    return False



