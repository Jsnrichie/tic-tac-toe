col_headings = list(' ' * 11)
col_headings[1] = 'A'
col_headings[5] = 'B'
col_headings[9] = 'C'

index = ['1 |', '2 |', '3 |']

row = " - | - | - "  # 1,5,9
divider = "-" * len(row)

positions = {
    "A": 1,
    "B": 5,
    "C": 9,
}


class Board:
    def __init__(self):
        self.new_board()
        self.last_letter = None

    def new_board(self):
        self.row1 = list(row)
        self.row2 = list(row)
        self.row3 = list(row)

    def display(self):
        print(f'''
   {''.join(col_headings)}
{index[0]}{''.join(self.row1)}
   {divider}
{index[1]}{''.join(self.row2)}
   {divider}
{index[2]}{''.join(self.row3)}
''')

    def play(self, pos, letter):
        self.last_letter = letter

        row = pos[0]
        column_index = positions[pos[1]]

        if row == '1':
            if self.row1[column_index] == '-':
                self.row1[column_index] = letter
                self.display()
                return True
            else:
                print('that position is already in use')
                return False
        elif row == '2':
            if self.row2[column_index] == '-':
                self.row2[column_index] = letter
                self.display()
                return True
            else:
                print('that position is already in use')
                return False
        elif row == '3':
            if self.row3[column_index] == '-':
                self.row3[column_index] = letter
                self.display()
                return True
            else:
                print('that position is already in use')
                return False
        else:
            print("invalid input")
            return False

    def check_winner(self):
        if self.row1[positions['A']] != "-" and (
                self.row1[positions['A']] == self.row1[positions['B']] == self.row1[positions['C']] or
                self.row1[positions['A']] == self.row2[positions['A']] == self.row3[positions['A']] or
                self.row1[positions['A']] == self.row2[positions['B']] == self.row3[positions['C']]
        ):
            return True

        elif self.row2[positions['B']] != "-" and (
                self.row2[positions['A']] == self.row2[positions['B']] == self.row2[positions['C']] or
                self.row1[positions['B']] == self.row2[positions['B']] == self.row3[positions['B']] or
                self.row3[positions['A']] == self.row2[positions['B']] == self.row1[positions['C']]
        ):
            return True
        elif self.row3[positions['C']] != "-" and (
                self.row3[positions['A']] == self.row3[positions['B']] == self.row3[positions['C']] or
                self.row1[positions['C']] == self.row2[positions['C']] == self.row3[positions['C']]
        ):
            return True
        else:
            return False

    def is_full(self):
        all_positions = [
            self.row1[positions['A']],
            self.row1[positions['B']],
            self.row1[positions['C']],
            self.row2[positions['A']],
            self.row2[positions['B']],
            self.row2[positions['C']],
            self.row3[positions['A']],
            self.row3[positions['B']],
            self.row3[positions['C']],
        ]

        for space in all_positions:
            if space == '-':
                return False

        return True

    def reveal_winner(self):
        if self.last_letter == 'X':
            print("PLAYER 1 WINS")
        else:
            print("PLAYER 2 WINS")
