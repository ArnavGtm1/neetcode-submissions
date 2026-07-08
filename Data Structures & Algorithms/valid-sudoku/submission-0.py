class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        map2 = {}
        for i in range(len(board)):
            row_set = set()
            col_set = set()
            for j in range(len(board[i])):
                #checking rows
                if(board[i][j]!= "."):
                    if(board[i][j] in row_set):
                        return False
                    row_set.add(board[i][j])

                #checking columns
                if board[j][i]!= ".":
                    if(board[j][i] in col_set):
                        return False
                    col_set.add(board[j][i])

                #checking boxes
                if board[i][j]!= ".":
                    boxIndex = ((i//3) * 3) + (j//3)
                    if(boxIndex in map2):
                        if(board[i][j] in map2[boxIndex]):
                            return False
                        map2[boxIndex].add(board[i][j])
                    else:
                        map2[boxIndex] = set([board[i][j]])
        
        return True

        


                 




