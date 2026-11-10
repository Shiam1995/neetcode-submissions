class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #print(len(board))
        #print(len(board[0]))


        for row in board:
            seen = set()
            for cell in row:
                if cell== '.':
                    continue
                if cell in seen: # could specific a valid range but question already says its there
                   # print("Row no good")
                    return False
                seen.add(cell)


        for col in range(len(board)):
           seen = set()
           for row in range(len(board)):
               cell = board[row][col]
               if cell == '.':
                   continue
               if cell in seen:  # could specific a valid range but question already says its there
                  # print("col no good")
                   return False
               seen.add(cell)

            # so whats being passed in


        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                seen = set()
                for row in range(box_row, box_row + 3):
                    for col in range(box_col, box_col + 3):
                        cell = board[row][col]
                        if cell == '.':
                            continue
                        if cell in seen:  # could specific a valid range but question already says its there
                            #print("box no good")
                            return False
                        seen.add(cell)








        # I could manually write the code for the cells boxes but I think leave it



        return True