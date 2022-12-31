'''The base game of tic tac toe'''

class board:
    def __init__(self):
        '''Sets up the board for the game.'''
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    def clearBoard(self):
        '''Clears the board'''
        '''[[The first row], [The second row], [The third row]]'''
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    def countChars(self, sym):
        '''Counts the number of syms(Xs, Os or blanks) on the board'''
        c = 0
        for i in self.board:
            for j in i:
                if j == sym:
                    c += 1
        return c

    def CheckTurn(self):
        '''Checks whose turn it is to move'''
        numX = self.countChars('X')
        numO = self.countChars('O')

        if numX < numO:
            raise Exception('Illegal board position! More Os than Xs')
        elif numX == numO:
            return 'X'
        else:
            return 'O'

    def set(self, sym, posY, posX):
        '''Place a sym(X or O) in coordinates Y, X (O <= X, Y <= 3)'''

        #Check if it is the correct player
        if sym != self.CheckTurn():
            raise Exception('The wrong turn!')

        #Check if the coordinate is already occupied
        if self.board[posY][posX] in 'XO':
            #print(self.board)
            raise Exception('The space is already occupied!')

        self.board[posY][posX] = sym

    def CheckBoard(self):
        '''Returns 0 if X wins, 1 if O wins, -1 if neither has won, 2 if draw'''

        #Win conditions - if PosX/PosY is the same for all 3 Xs, Os (or) [(0, 0), (1, 1), (2, 2)] (or) [(2, 0), (1, 1), (0, 2)]
        xPos = [[], []]
        oPos = [[], []]
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 'X':
                    xPos[0].append(i)
                    xPos[1].append(j)
                elif self.board[i][j] == 'O':
                    oPos[0].append(i)
                    oPos[1].append(j)

        def changeIterationType(L):
            n = len(L[0])
            tempList = []
            for i in range(n):
                tempList.append((L[0][i], L[1][i]))
            return tempList

        #Checking rows and columns
        for i in range(3):
            if xPos[0].count(i) == 3 or xPos[1].count(i) == 3:
                return 0
            elif oPos[0].count(i) == 3 or oPos[1].count(i) == 3:
                return 1

        #Checking the diagonals
        xPos = changeIterationType(xPos)
        oPos = changeIterationType(oPos)
        if all(x in xPos for x in [(0, 0), (1, 1), (2, 2)]) or all(x in xPos for x in [(2, 0), (1, 1), (0, 2)]):
            return 0
        elif all(x in oPos for x in [(0, 0), (1, 1), (2, 2)]) or all(x in oPos for x in [(2, 0), (1, 1), (0, 2)]):
            return 1

        # Checking for draw
        c = 0
        for i in self.board:
            if ' ' in i:
                break
        else:
            return 2

        return -1

    def printBoard(self):
        '''Displays the board (for debug)'''
        for i in self.board:
            print(i)

