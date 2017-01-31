#endView.py
#Anna Marek
#5/10/16

import copy
from graphics import *

def modeMenu():
    print("1. Muli-Puzzle File upload")
    print("2. Single-Puzzle File upload")
    print("3. User input")
    print("0. Exit")
    return int(input("Selection: "))

def printMenu():
    print("1. Muli-Puzzle File upload")
    print("2. Single-Puzzle File upload")
    print("3. User input")
    print("0. Exit")

def solve():
    selection = modeMenu()
    #printOpt = printMenu()
    yay = 0
    nay = 0
    fail = 0
    yays = open("yay.txt","w")
    nays = open("nay.txt","w")
    fails = open("fail.txt","w")
    nayboards = open("tryAgain.txt","w")
    while selection != 0:
        if selection == 1:
            #fileName = input("(Make sure your file is of the format PUZZLENUM, SIZE, POSSIBLES, TOP, RIGHT, BOTTOM, LEFT)\n What if your file name? ")
            fileName = "puzzle480.txt"
            infile = open(fileName, 'r')
            num = int(next(infile).strip())
            size = int(next(infile).strip())
            possibles = list(next(infile).strip().upper())
            possibles.sort()
            t = list(next(infile).strip().upper())
            r = list(next(infile).strip().upper())
            b = list(next(infile).strip().upper())
            l = list(next(infile).strip().upper())
        elif selection == 2:
            fileName = input("(Make sure your file is of the format SIZE, POSSIBLES, TOP, RIGHT, BOTTOM, LEFT)\n What if your file name? ")
            infile = open(fileName, 'r')
            size = int(next(infile).strip())
            possibles = list(next(infile).strip().upper())
            possibles.sort()
            t = list(next(infile).strip().upper())
            r = list(next(infile).strip().upper())
            b = list(next(infile).strip().upper())
            l = list(next(infile).strip().upper())
        elif selection == 3:
            size = int(input("What is the size of your board? (Enter a single number) "))
            possibles = list(input("Enter the possible lettters in the puzzle with no spaces or dashes (don't mess up, I'm too lazy to input validate this): ").upper())
            possibles.sort()
            print("When entering clues enter either left to right or top to bottom")
            t = list(input("Enter the top clues (enter - for blank clues) ").upper())
            r = list(input("Enter the right clues (enter - for blank clues) ").upper())
            b = list(input("Enter the bottom clues (enter - for blank clues) ").upper())
            l = list(input("Enter the left clues (enter - for blank clues) ").upper())
        elif selection == -1:
            num = test
            size = int(next(infile).strip())
            possibles = list(next(infile).strip().upper())
            possibles.sort()
            t = list(next(infile).strip().upper())
            r = list(next(infile).strip().upper())
            b = list(next(infile).strip().upper())
            l = list(next(infile).strip().upper())
        #print(num)
        solved = True
        used = []
        xPos = []
        clues = [t,r,b,l]
        board = [[["-" for i in range(len(possibles))] for x in range(size)] for y in range(size)]
        oldBoard = []
        #graphBoard = createBoard(size, clues)
        while board != oldBoard:
            oldBoard = copy.deepcopy(board)
            failedBoard = False
            
            try:
                #Mark up
                pre = copy.deepcopy(board)
                checkClues(board,clues,possibles)
    ##            if pre != board:
    ##                print("Check clues")
    ##                print("Pre:")
    ##                printBoard(pre)
    ##                print("After:")
    ##                printBoard(board)

                pre = copy.deepcopy(board)
                process2(board, clues, possibles)
    ##            if pre != board:
    ##                print("p2")
    ##                print("Pre:")
    ##                printBoard(pre)
    ##                print("After:")
    ##                printBoard(board)

                pre = copy.deepcopy(board)
                checkRC(board)
    ##            if pre != board:
    ##                print("Check RC")
    ##                print("Pre:")
    ##                printBoard(pre)
    ##                print("After:")
    ##                printBoard(board)

                pre = copy.deepcopy(board)
                process4(board, clues, possibles)
    ##            if pre != board:
    ##                print("p4")
    ##                print("Pre:")
    ##                printBoard(pre)
    ##                print("After:")
    ##                printBoard(board)

                pre = copy.deepcopy(board)
                process5(board, clues, possibles)
    ##            if pre != board:
    ##                print("p5")
    ##                print("Pre:")
    ##                printBoard(pre)
    ##                print("After:")
    ##                printBoard(board)

                pre = copy.deepcopy(board)
                process8(board, clues)
    ##            if pre != board:
    ##                print("p8")
    ##                print("Pre:")
    ##                printBoard(pre)
    ##                print("After:")
    ##                printBoard(board)

                #Make Conclusions
                pre = copy.deepcopy(board)
                markEmpty(board, xPos)
    ##            if pre != board:
    ##                print("Mark Empty")
    ##                print("Pre:")
    ##                printBoard(pre)
    ##                print("After:")
    ##                printBoard(board)
                
                pre = copy.deepcopy(board)
                markLetters(board, possibles)
    ##            if pre != board:
    ##                print("Mark Letters")
    ##                print("Pre:")
    ##                printBoard(pre)
    ##                print("After:")
    ##                printBoard(board)

                pre = copy.deepcopy(board)
                process6(board, xPos, possibles)
    ##            if pre != board:
    ##                print("p6")
    ##                print("Pre:")
    ##                printBoard(pre)
    ##                print("After:")
    ##                printBoard(board)

                pre = copy.deepcopy(board)
                process7(board, clues, possibles)
    ##            if pre != board:
    ##                print("p7")
    ##                print("Pre:")
    ##                printBoard(pre)
    ##                print("After:")
    ##                printBoard(board)
            except:
                failedBoard = True

        if failedBoard:
            fail += 1
            fails.write(str(num)+"\n")
        else:
            for i in board:
                for j in i:
                    if len(j) > 1:
                        solved = False

            if solved:
                yay += 1
                yays.write(str(num)+"\n")
            else:
                for i in board:
                    for j in i:
                        if len(j) == 1:
                            if i.count(j) > 1:
                                failedBoard = True
                if failedBoard:
                    fail += 1
                    fails.write(str(num)+"\n")
                else:
                    nay += 1
                    nays.write(str(num)+"\n")
                    nayboards.write(str(num)+"\n")
                    writeBoard(nayboards, board)
                
        if selection == 1 or selection == -1:
            try:
                test = int(next(infile).strip())
                selection = -1
            except StopIteration:
                yays.write("total: "+str(yay))
                nays.write("total: "+str(nay))
                selection = modeMenu()
        elif selection == 3:
            print("Final:")
            printBoard(board)
            selection = modeMenu()
        elif selection == 2:
            print("Final:")
            printBoard(board)
            selection = modeMenu()
        else:
            selection = modeMenu()
    
def printBoard(board):
    draw = False
    n = 0
    for i in board:
        for j in i:
            for l in j:
                print(l, end="")
            print("\t",end="")
        print("\n")
    print("\n")

def printGraphicsBoard(graphBoard, used):
    draw = False
    n = 0
    for i in board:
        m = 0
        for j in i:
            if len(board[n][m])==1:
                if (n,m) not in used:
                    draw = True
                    used.append((n,m))
                    txt = Text(Point(50*(m+1),50*(n+1)),board[n][m])
                    txt.setSize(30)
                    txt.draw(graphBoard)
            m += 1
        n += 1
    if draw:
        graphBoard.getMouse()

def writeBoard(outfile, board):
    n = 0
    for i in board:
        for j in i:
            for l in j:
                outfile.write(l)
            outfile.write("\t")
        outfile.write("\n")
    outfile.write("\n")

def createBoard(size, clues):
    t = clues[0]
    r = clues[1]
    b = clues[2]
    l = clues[3]
    win = GraphWin("Board", 50*(size+1), 50*(size+1))
    for i in range(size):
        for j in range(size):
            s = Rectangle(Point((i*50)+25,(i*50)+25), Point((j*50)+75,(j*50)+75))
            s.draw(win)

        txt = Text(Point(50*(i+1), 15), t[i])
        txt.draw(win)

        txt = Text(Point(50*(i+1), (50*(size+1))-15), b[i])
        txt.draw(win)

        txt = Text(Point(15, 50*(i+1)), l[i])
        txt.draw(win)

        txt = Text(Point((50*(size+1))-15,50*(i+1)), r[i])
        txt.draw(win)
    win.getMouse() # pause for click in window
    return win
    

def validateClue(size, clue):
    #Not currently working
    while len(clue) != size or " " in clue:
        clue = list(input("Yeah, try that again: ").upper())

def checkClues(board, clues, possibles):
    t = clues[0]
    r = clues[1]
    b = clues[2]
    l = clues[3]
    j = 0
    while j < len(board):

        if t[j] != "-":
            p = possibles.copy()
            p[ord(t[j])-65] = '-'
            if len(board[0][j]) > 1:
                for c in range(len(board[0][j])):
                    if board[0][j][c] == '-':
                        board[0][j][c] = p[c]
                
            elif board[0][j] == 'X':
                m = 0
                while board[m][j] == 'X' and m < len(board):
                    m += 1
                for c in range(len(board[m][j])):
                    if board[m][j][c] == '-':
                        board[m][j][c] = p[c]

        if b[j] != "-":
            p = possibles.copy()
            p[ord(b[j])-65] = '-'
            if len(board[-1][j]) > 1:
                for c in range(len(board[-1][j])):
                    if board[-1][j][c] == '-':
                        board[-1][j][c] = p[c]
            elif board[-1][j] == 'X':
                m = -1
                while board[m][j] == 'X' and m < len(board):
                    m -= 1
                for c in range(len(board[m][j])):
                    if board[m][j][c] == '-':
                        board[m][j][c] = p[c]
                
        j += 1
        
    i = 0
    while i < len(board):

        if r[i] != "-":
            p = possibles.copy()
            p[ord(r[i])-65]='-'
            if len(board[i][-1]) > 1:
                for c in range(len(board[i][-1])):
                    if board[i][-1][c] == '-':
                        board[i][-1][c] = p[c]
            elif board[i][-1] == 'X':
                n = -1
                while board[i][n] == 'X' and n < len(board):
                    n -= 1
                for c in range(len(board[i][n])):
                    if board[i][n][c] == '-':
                        board[i][n][c] = p[c]
    
        if l[i] != "-":
            p = possibles.copy()
            p[ord(l[i])-65]='-'
            if len(board[i][0]) > 1:
                for c in range(len(board[i][0])):
                    if board[i][0][c] == '-':
                        board[i][0][c] = p[c]
            elif board[i][0] == 'X':
                n = 0
                while board[i][n] == 'X' and n < len(board):
                    n += 1
                for c in range(len(board[i][n])):
                    if board[i][n][c] == '-':
                        board[i][n][c] = p[c]
        i += 1

def process2(board, clues, possibles):
    ##Okay, we're going to have to name these stupid things later.
    ##Basically, I'm doing the thing I do where I don't allow clues
    ##from one edge to close to the edge on the other side... Send help
    pnum = len(possibles)-1
    t = clues[0]
    r = clues[1]
    b = clues[2]
    l = clues[3]
    j = 0
    while j < len(board):

        if t[j] != "-":
            c = 0
            n = len(board)-1
            p = ord(t[j])-65
            while c < pnum:
                if board[n][j] != 'X':
                    if len(board[n][j]) > 1:
                        board[n][j][p] = t[j]
                    c += 1
                n -= 1

        if b[j] != "-":
            c = 0
            n = 0
            p = ord(b[j])-65
            while c < pnum:
                if board[n][j] != 'X':
                    if len(board[n][j]) > 1:
                        board[n][j][p] = b[j]
                    c += 1
                n += 1
        j += 1
        
    i = 0
    while i < len(board):

        if r[i] != "-":
            c = 0
            m = 0
            p = ord(r[i])-65
            while c < pnum:
                if board[i][m] != 'X':
                    if len(board[i][m]) > 1:
                        board[i][m][p] = r[i]
                    c += 1
                m += 1
    
        if l[i] != "-":
            c = 0
            m = len(board)-1
            p = ord(l[i])-65
            while c < pnum:
                if board[i][m] != 'X':
                    if len(board[i][m]) > 1:
                        board[i][m][p] = l[i]
                    c += 1
                m -= 1
        i += 1

def checkRC(board):
    ##Okay, we're going to have to name these stupid things later.
    ##This one checks rows and columns for letters
    for i in range(len(board)):
        for j in range(len(board)):
            if len(board[i][j])==1 and board[i][j] != 'X':
                c = board[i][j]
                for n in range(len(board)):
                    if len(board[n][j]) > 1:
                        board[n][j][ord(board[i][j])-65]=board[i][j]
                for m in range(len(board)):
                    if len(board[i][m]) > 1:
                        board[i][m][ord(board[i][j])-65]=board[i][j]

def process4(board, clues, possibles):
    ##Uhm... so if there's multiple of the same clue on a side then
    ##a thing happens
    t = clues[0]
    r = clues[1]
    b = clues[2]
    l = clues[3]
    multiples = []
    for c in t:
        if c != '-':
            if t.count(c) > 1:
                multiples.append(c)
    multiples = set(multiples)
    if len(multiples) > 0:
        for multiple in multiples:
            if len(board)-len(possibles) == t.count(multiple)-1:
                j = 0
                while j < len(board):
                    if t[j] != multiple:
                        for n in range(t.count(multiple)):
                            p = ord(multiple)-65
                            if len(board[n][j]) > 1:
                                board[n][j][p] = multiple
                    j += 1
    multiples = []
    for c in b:
        if c != '-':
            if b.count(c) > 1:
                multiples.append(c)
    multiples = set(multiples)
    if len(multiples) > 0:
        for multiple in multiples:
            if len(board)-len(possibles) == b.count(multiple)-1:
                j = 0
                while j < len(board):
                    if b[j] != multiple:
                        for n in range(b.count(multiple)):
                            p = ord(multiple)-65
                            if len(board[n+(len(possibles)-1)][j]) > 1:
                                board[n+(len(possibles)-1)][j][p] = multiple
                    j += 1
    multiples = []
    for c in l:
        if c != '-':
            if l.count(c) > 1:
                multiples.append(c)
    multiples = set(multiples)
    if len(multiples) > 0:
        for multiple in multiples:
            if len(board)-len(possibles) == l.count(multiple)-1:
                i = 0
                while i < len(board):
                    if l[i] != multiple:
                        for m in range(l.count(multiple)):
                            p = ord(multiple)-65
                            if len(board[i][m]) > 1:
                                board[i][m][p] = multiple
                    i += 1
    multiples = []
    for c in r:
        if c != '-':
            if r.count(c) > 1:
                multiples.append(c)
    multiples = set(multiples)
    if len(multiples) > 0:
        for multiple in multiples:
            if len(board)-len(possibles) == r.count(multiple)-1:
                i = 0
                while i < len(board):
                    if r[i] != multiple:
                        for m in range(r.count(multiple)):
                            p = ord(multiple)-65
                            if len(board[i][m+(len(possibles)-1)]) > 1:
                                board[i][m+(len(possibles)-1)][p] = multiple
                    i += 1

def process5(board, clues, possibles):
    ##Kay, so if the number of X's is the size of the board minus the depth on
    ##an edge, then that forces the clues on that edge to manifest immediately
    t = clues[0]
    r = clues[1]
    b = clues[2]
    l = clues[3]
    if board[0].count('X') == len(board) - len(possibles):
        m = 0
        for j in board[0]:
            if t[m] != '-':
                if board[0][m] != 'X':
                    board[0][m] = t[m]
            m += 1
    if board[-1].count('X') == len(board) - len(possibles):
        m = 0
        for j in board[-1]:
            if b[m] != '-':
                if board[-1][m] != 'X':
                    board[-1][m] = b[m]
            m += 1
    Xs = 0
    n = 0
    for i in board:
        if board[n][0] == 'X':
            Xs += 1
        n += 1
    if Xs == len(board) - len(possibles):
        n = 0
        for i in board:
            if l[n] != '-':
                if board[n][0] != 'X':
                    board[n][0] = l[n]
            n += 1
    Xs = 0
    n = 0
    for i in board:
        if board[n][-1] == 'X':
            Xs += 1
        n += 1
    if Xs == len(board) - len(possibles):
        n = 0
        for i in board:
            if r[n] != '-':
                if board[n][-1] != 'X':
                    board[n][-1] = r[n]
            n += 1

def process6(board, xPos, possibles):
    ##Checking for places for X's based on the positions of other X's
    n = 0
    for i in board:
        es = 0
        xs = 0
        if i.count('X') < len(board) - len(possibles):
            m = 0
            for j in i:
                e = True
                if len(j) > 1:
                    es += 1
                    p = 0
                    x = 0
                    for pos in xPos:
                        if xPos[p][1] == m:
                            x += 1
                            if x == len(board) - len(possibles):
                                xs += 1
                                e = False
                        p += 1
                    if e:
                        empty = (n,m)
                m += 1
        n += 1
        if es - xs == 1:
            board[empty[0]][empty[1]] = 'X'
            xPos.append((empty[0],empty[1]))
            
    for i in board:
        m = 0
        for j in i:
            es = 0
            xs = 0
            rowX = 0
            r = 0
            for row in board:
                if board[r][m] == 'X':
                    rowX += 1
                r += 1
            if rowX < len(board) - len(possibles):
                n = 0
                for i2 in board:
                    e = True
                    if len(board[n][m]) > 1:
                        es += 1
                        p = 0
                        x = 0
                        for pos in xPos:
                            if xPos[p][0] == n:
                                x += 1
                                if x == len(board) - len(possibles):
                                    xs += 1
                                    e = False
                            p += 1
                        if e:
                            empty = (n,m)
                    n += 1
            m += 1
            if es - xs == 1:
                board[empty[0]][empty[1]] = 'X'
                xPos.append((empty[0],empty[1]))
        

def process7(board, clues, possibles):
    ##Alrighty, if there's multiple of a clue on an edge, it'll force X's
    ##and therefore force other edge clues to be immediate
    t = clues[0]
    r = clues[1]
    b = clues[2]
    l = clues[3]
    multiples = []
    for c in t:
        if c != '-':
            if t.count(c) > 1:
                multiples.append(c)
    multiples = set(multiples)
    if len(multiples) > 0:
        xs = 0
        for multiple in multiples:
            xs += (t.count(multiple)-1)
        if len(board)-len(possibles) == xs:
            j = 0
            while j < len(board):
                if t[j] not in multiples:
                    if t[j] != "-":
                        board[0][j] = t[j]
                j += 1
    multiples = []
    for c in b:
        if c != '-':
            if b.count(c) > 1:
                multiples.append(c)
    multiples = set(multiples)
    if len(multiples) > 0:
        xs = 0
        for multiple in multiples:
            xs += (b.count(multiple)-1)
        if len(board)-len(possibles) == xs:
            j = 0
            while j < len(board):
                if b[j] not in multiples:
                    if b[j] != "-":
                       board[-1][j] = b[j]
                j += 1
    multiples = []
    for c in l:
        if c != '-':
            if l.count(c) > 1:
                multiples.append(c)
    multiples = set(multiples)
    if len(multiples) > 0:
        xs = 0
        for multiple in multiples:
            xs += (l.count(multiple)-1)
        if len(board)-len(possibles) == xs:
            i = 0
            while i < len(board):
                if l[i] not in multiples:
                    if l[i] != "-":
                        board[i][0] = l[i]
                i += 1
    multiples = []
    for c in r:
        if c != '-':
            if r.count(c) > 1:
                multiples.append(c)
    multiples = set(multiples)
    if len(multiples) > 0:
        xs = 0
        for multiple in multiples:
            xs += (r.count(multiple)-1)
        if len(board)-len(possibles) == xs:
            i = 0
            while i < len(board):
                if r[i] not in multiples:
                    if r[i] != "-":
                        board[i][-1] = r[i]
                i += 1

def process8(board, clues):
    ##Uhm, if the box two spaces in is filled with a letter, then 
    ##a clue will be satisfied immediately
    t = clues[0]
    r = clues[1]
    b = clues[2]
    l = clues[3]
    j = 0
    while j < len(board):

        inCol = False
        if t[j] != "-":
            if len(board[1][j]) == 1 and board[1][j] != 'X':
                rNum = 0
                for row in board:
                    if board[rNum][j] == t[j]:
                        inCol = True
                    rNum += 1
                if not inCol:
                    board[0][j] = t[j]

        if b[j] != "-":
            if len(board[-2][j]) == 1 and board[-2][j] != 'X':
                rNum = 0
                for row in board:
                    if board[rNum][j] == b[j]:
                        inCol = True
                    rNum += 1
                if not inCol:
                    board[-1][j] = b[j]
                
        j += 1
        
    i = 0
    while i < len(board):

        if r[i] != "-":
            if len(board[i][-2]) == 1 and board[i][-2] != 'X':
                if r[i] not in board[i]:
                    board[i][-1] = r[i]
    
        if l[i] != "-":
            if len(board[i][1]) == 1 and board[i][1] != 'X':
                if l[i] not in board[i]:
                    board[i][0] = l[i]

        i += 1
                                                  
def markEmpty(board, xPos):
    i=0
    for row in board:
        j=0
        for col in row:
            if len(col) > 1:
                if "-" not in board[i][j]:
                    board[i][j] = 'X'
                    xPos.append((i,j))
            j+=1
        i+=1

def markLetters(board, possibles):
    i = 0
    while i < len(board):
        for p in possibles:
            c = 0
            pindex = ord(p)-65
            for m in range(len(board)):
                if board[i][m] == p:
                    c = len(board)
                if len(board[i][m]) == 1:
                    c += 1
                elif board[i][m][pindex] == p:
                    c += 1
                else:
                    save = m
            if len(board)-c == 1:
                board[i][save] = p
        i += 1
    j = 0

    while j < len(board):
        for p in possibles:
            c = 0
            pindex = ord(p)-65
            for n in range(len(board)):
                if board[n][j] == p:
                    c = len(board)
                elif len(board[n][j]) == 1:
                    c += 1
                elif board[n][j][pindex] == p:
                    c += 1
                else:
                    save = n
            if len(board)-c == 1:
                board[save][j] = p
        j += 1
