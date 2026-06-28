import numpy as np

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(len(board)):
            lst = board[i]
            curr_row = [item for item in lst if item.isalnum()]
            print("Curr row: ", curr_row)
            if len(curr_row) != len(list(set(curr_row))):
                return False
        

        new_arr = np.array(board)
        board_transpose = np.transpose(new_arr).tolist()

        for i in range(len(board_transpose)):
            lst = board_transpose[i]
            curr_row = [item for item in lst if item.isalnum()]
            print("Curr row: ", curr_row)
            if len(curr_row) != len(list(set(curr_row))):
                return False
        
        return True
