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
                    board[i][0] = l[j]
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
                    board[i][0] = r[j]
                i += 1
