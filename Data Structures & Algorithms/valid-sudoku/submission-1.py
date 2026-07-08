class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        import collections
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Initialize dictionaries where every new key automatically starts with an empty set
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                # Skip empty cells
                if val == ".":
                    continue
                
                # Calculate the 3x3 box index using a tuple (row // 3, col // 3)
                box_index = (r // 3, c // 3)

                # Check for duplicates in the current row, column, or 3x3 box
                if (val in rows[r]) or (val in cols[c]) or (val in boxes[box_index]):
                    return False
                
                # If no duplicates, add the value to our tracking sets
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_index].add(val)
        
        return True