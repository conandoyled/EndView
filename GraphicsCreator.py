from graphics import *

win = GraphWin("Board", 50*(2+1), 50*(2+1))
txt = Text(Point(50*(2+1), 15), "Hello")
image = Image(Point(75,75),150,150)
txt.draw(win)
image.save("Help.gif")

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
