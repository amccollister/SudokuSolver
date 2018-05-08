class Square:
    def __init__(self, row, col):
        self._row = row
        self._col = col
        self._quadrant = 0
        self._value = 0
        self._choice = []

    @property
    def row(self):
        return self._row

    @property
    def col(self):
        return self._col

    @property
    def value(self):
        return self._value

    @property
    def choice(self):
        return self._choice

    @property
    def quadrant(self):
        return self._quadrant

    @row.setter
    def row(self, val):
        self._row = val

    @col.setter
    def col(self, val):
        self._col = val

    @value.setter
    def value(self, val):
        self._value = val

    @quadrant.setter
    def quadrant(self, val):
        self._quadrant = val

    @choice.setter
    def choice(self, val):
        self._choice = val

