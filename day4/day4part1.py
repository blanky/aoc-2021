#!/usr/bin/env python3


class BingoNumber:
    marked = False
    def __init__(self, number):
        self.number = number

# Hardcode 5x5 bingo board
class BingoBoard:
    WIN_CONDITIONS = [[0,1,2,3,4],
                      [5,6,7,8,9],
                      [10,11,12,13,14],
                      [15,16,17,18,19],
                      [20,21,22,23,24],
                      [0,5,10,15,20],
                      [1,6,11,16,21],
                      [2,7,12,17,22],
                      [3,8,13,18,23],
                      [4,9,14,19,24]]
    def __init__(self, numbers):
        self.bingo_numbers = list()
        for i in numbers:
            self.bingo_numbers.append(BingoNumber(i))
    
    def _line_bingo_checker(self, positions):
        return self.bingo_numbers[positions[0]].marked and self.bingo_numbers[positions[1]].marked and \
               self.bingo_numbers[positions[2]].marked and self.bingo_numbers[positions[3]].marked and \
               self.bingo_numbers[positions[4]].marked
    
    def _bingo_checker(self):
        for win_condition in self.WIN_CONDITIONS:
            if(self._line_bingo_checker(win_condition)):
                return True
        return False
    
    def print_board(self):
        board_str = ""
        for i in range(5):
            for j in range(5):
                number = self.bingo_numbers[i*5+j]
                board_str += "\033[92m%i\033[0m " % (number.number) if number.marked else "%i " % (number.number)
            board_str += "\n"
        print(board_str)

    def marker(self, new_match):
        for number in self.bingo_numbers:
            if number.number == new_match:
                number.marked = True
                if(self._bingo_checker()):
                    return 1
                else:
                    return 0
        return -1
    
    def unmarked_sum(self):
        sum = 0
        for num in self.bingo_numbers:
            if(num.marked == False):
                sum += num.number
        return sum
        

bingo_boards = list()

# with open("test.txt") as f:
with open("input.txt") as f:
    numbers = list(map(int, f.readline().split(',')))
    f.readline()
    text = f.readlines()
    for i in range(0, len(text), 6):
        bingo_text = text[i] + text[i+1] + text[i+2] + text[i+3] + text[i+4]
        bingo_numbers = map(int, filter(None, bingo_text.replace('\n', ' ').split(' ')))
        bingo_boards.append(BingoBoard(bingo_numbers))

for match in numbers:
    for bingo_board in bingo_boards:
        result = bingo_board.marker(match)
        if(result == 1):
            print("BINGO")
            bingo_board.print_board()
            print("Winning number: %i" % (match))
            print("Unmarked sum: %i" % (bingo_board.unmarked_sum()))
            print("Score: %i" % (match*bingo_board.unmarked_sum()))
            exit()

