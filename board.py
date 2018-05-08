from square import Square

class Board:
    def __init__(self):
        self._board = []
        self._guess = []
        self.make_board()
        self.RANGE = list(range(1, 10))

    def make_board(self):
        self._board = [[Square(i, j) for j in range(9)] for i in range(9)]
        self.set_quadrant()

    def set_quadrant(self):
        for i in range(9):
            for j in range(9):
                self._board[i][j].quadrant = (i//3*3)+j//3

    def print(self):
        for i in range(9):
            line = []
            for j in range(9):
                line.append(str(self._board[i][j].value))
            print(" ".join(line))

    def check_choice(self):
        for i in range(9):
            for j in range(9):
                sq = self.get_square(i, j)
                if(sq.choice == [] and sq.value == 0):
                    print("I see an issue at {} {}".format(i, j))
                    return True
        return False

    def set_square(self, row, col, val):
        self._board[row][col].value = val

    def get_square(self, row, col):
        return self._board[row][col]
    
    def check_board(self):
        for i in range(9):
            for j in range(9):
                if self._board[i][j].value == 0:
                    return False
        return True
    
    def establish_choices(self):
        for i in range(9):
            for j in range(9):
                sq = self.get_square(i, j)
                if sq.value == 0:
                    sq.choice = self.valid_choice(i, j, sq.quadrant)

    def validate_board(self):
        good = True
        for i in range(9):
            for j in range(9):
                row_choice = self.valid_row(i)
                col_choice = self.valid_col(j)
                quad_choice = self.valid_quadrant(self.get_square(i, j).quadrant)
                result = row_choice + col_choice + quad_choice
                if result != []:
                    good = False
                    break
        return good

    def valid_choice(self, row, col, quadrant):
        row_choice = self.valid_row(row)
        col_choice = self.valid_col(col)
        quad_choice = self.valid_quadrant(quadrant)
        return list(set(row_choice) & set(col_choice) & set(quad_choice))

    def valid_row(self, row):
        valid = self.RANGE[:]
        for i in range(9):
            sq = self.get_square(row, i)
            if sq.value in valid:
                valid.remove(sq.value)
        return valid

    def valid_col(self, col):
        valid = self.RANGE[:]
        for i in range(9):
            sq = self.get_square(i, col)
            if sq.value in valid:
                valid.remove(sq.value)
        return valid

    def valid_quadrant(self, quadrant):
        valid = self.RANGE[:]
        for i in range(9):
            for j in range(9):
                sq = self.get_square(i, j)
                if quadrant == sq.quadrant and sq.value in valid:
                    valid.remove(sq.value)
        return valid
                
    def fill_single_choice(self):
        for i in range(9):
            for j in range(9):
                sq = self.get_square(i, j)
                if sq.value == 0 and len(sq.choice) == 1:
                    sq.value = sq.choice[0]
                    sq.choice = []
                    if len(self.guess) > 0:
                        self.guess.append(sq)
                    return True
        return False

    def make_guess(self):
        for i in range(9):
            for j in range(9):
                sq = self.get_square(i, j)
                if sq.value == 0 and sq.choice != []:
                    sq.value = sq.choice[0]
                    sq.choice.pop(0)
                    self.guess.append(sq)
                    return sq
                    
    @property
    def guess(self):
        return self._guess

    @guess.setter
    def guess(self, val):
        self._guess = val

    def reset_guess(self):
        for i, g in reversed(list(enumerate(self.guess))):
            if g.choice != []:
                g.value = g.choice.pop(0)
                return
            else:
                g.value = 0
                self.guess.remove(g)
