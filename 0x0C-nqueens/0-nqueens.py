#!/usr/bin/python3
"""
Module - nqueens
"""
import sys
import math

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)
try:
    size = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    exit(1)
if size < 4:
    print("N must be at least 4")
    exit(1)


def nqueens(n):
    """
    function - Solves N-queens Problem
    """
    all_ones = 2 ** n - 1
    count = 0
    board = []
    for i in range(n):
        j = [0, 0]
        board.append(j)

    def bitCheck(board, row, ld, column, rd):
        """
        ld - left diagonal conflict binary check
        rd - right diagonal conflict binary check
        column - columns conflict binary check
        row - rows conflict binary check
        count - number of valid solutions
        """
        nonlocal count

        if column == all_ones:
            count += 1
            print(board)
            return
        possibleSlots = ~(ld | column | rd) & all_ones
        while possibleSlots:
            currentBit = possibleSlots & -possibleSlots
            possibleSlots -= currentBit
            col = (int)(math.log(currentBit)/math.log(2))
            board[row] = [row, col]
            bitCheck(board, row + 1, (ld | currentBit) >> 1,
                     column | currentBit,
                     (rd | currentBit) << 1)

    bitCheck(board, 0, 0, 0, 0)
    return count

nqueens(size)
