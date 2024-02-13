# Author: Kristin Towns
# GitHub username: kristinlashun
# Date: 2/12/2024
# Description: This file contains a recursive function named row_puzzle that determines if a given puzzle (a list of integers) 
# can be solved. The puzzle is solved if a token, starting from the first square, can reach the last square based on the rules 
# defined (it can move a number of squares equal to the value of the current square).

def row_puzzle(row, position=0, visited=None):
    # If this is the first call, create a set to track visited positions
    if visited is None:
        visited = set()
    
    # Base case: if the position is at the last index, puzzle is solvable
    if position == len(row) - 1:
        return True

    # If the position is already visited, we are in a loop, so return False
    if position in visited:
        return False

    # Add current position to the set of visited positions
    visited.add(position)

    # Try moving to the right
    if position + row[position] < len(row):
        if row_puzzle(row, position + row[position], visited):
            return True

    # Try moving to the left
    if position - row[position] >= 0:
        if row_puzzle(row, position - row[position], visited):
            return True

    # If neither moving right nor left leads to a solution, return False
    # Before returning, remove the current position from visited to not affect subsequent calls
    visited.remove(position)
    return False