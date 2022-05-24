import operator
from itertools import product, permutations
import numpy as np


def calculate(numbers, target, op):
    operator_dict = {"+": operator.add,
                     "-": operator.sub,
                     "*": operator.mul,
                     "/": operator.truediv}

    running_total = numbers[0]
    for number in numbers[1:]:
        running_total = operator_dict[op](running_total, number)

    if running_total == target:
        return True
    return False

def valid_number(row, column, board, size):
    valid_column = set()
    for number in range(1, size + 1):
            valid_column.add(number)
    valid_numbers = valid_column
    yield from valid_numbers

def is_valid_sum(board, instruction_array, number_groups):
    for group in range(1, number_groups + 1):
        coordinates = []
        list_numbers = []
        next_group = 0
        for i, j in product([row for row in range(size)], [column for column in range(size)]):
            if instruction_array[i][j][0] == group:
                if instruction_array[row][column][2] == '=':
                    next_group = 1
                    break
                target = instruction_array[i][j][1]
                op = instruction_array[i][j][2]
                list_numbers.append(int(board[i, j]))
        if next_group == 1:
            continue
        combination_numbers = permutations(list_numbers, len(list_numbers))
        for combination in combination_numbers:
            target_reached = calculate(combination, target, op)
            if target_reached:
                break
        if target_reached:
            continue
        else:
            return False
    return True

def is_full(board, size):
    for row in range(size):
        for column in range(size):
            if board[row, column] == 0:
                return False
    return True

def check_number(board,i,j):
    for k in range(0, size ):
        if ((board[i,j]== board[k,j])&(k !=i)) :
            return 1
        if ((board[i,j]== board[i,k])&(k!=j)):
            return 1


def solve_board(board, instruction_array, size, number_groups, domain):
    if is_full(board, size):
        if is_valid_sum(board, instruction_array, number_groups):
            return True, board
        return False, board
    for i, j in product([row for row in range(size)],
                        [column for column in range(size)]):  # Product is from itertools library
        if board[i, j] != 0:
            continue
        for number in  domain:
            board[i, j] = number
            ################
            checking = check_number(board, i, j)
            if(checking):
                board[i,j]=0
                continue
            ################
            is_solved, board = solve_board(board, instruction_array, size, number_groups, domain)
            if is_solved:
                return True, board
            board[i, j] = 0
        return False, board
    return False, board


def fill_obvious(board, instruction_array, size):
    # Fill fixed numbers
    for row in range(size):
        for column in range(size):
            if instruction_array[row][column][2] == '=':
                board[row, column] = instruction_array[row][column][1]
    return board


if __name__ == "__main__":
    instruction_array =[
        [[1, 6, '*'], [2, 3, '='], [3, 6, '*']], 
        [[1, 6, '*'], [1, 6, '*'], [3, 6, '*']], 
        [[4, 2, '='], [1, 6, '*'], [3, 6, '*']]
        ]

    size = len(instruction_array[0])
    number_groups=0
    for row in range(size):
        for column in range(size):
            if(instruction_array[row][column][0]> number_groups):
                number_groups=instruction_array[row][column][0]

    #get the domain of numbers for the board
    domain=[]
    for i in range(1,size+1):
         domain.append(i)
    board = np.zeros(size * size).reshape(size, size)
    board = fill_obvious(board, instruction_array, size)
    is_solved, solved = solve_board(board, instruction_array, size, number_groups, domain)
    if is_solved:
        print(solved)
    else:
        print("Cannot solve")