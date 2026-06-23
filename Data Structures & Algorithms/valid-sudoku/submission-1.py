class Solution:

    def isRowValid(self, board: List[List[str]], row_num: int) -> bool:
        tracker = {}
        for i in range(0, 9):
            if board[row_num][i] == ".":
                next
            elif board[row_num][i] in tracker:
                return False
            else:
                tracker[board[row_num][i]] = 1
        return True

    def isColumnValid(self, board: List[List[str]], column_num: int) -> bool:
        tracker = {}
        for i in range(0, 9):
            if board[i][column_num] == ".":
                next 
            elif board[i][column_num] in tracker:
                return False
            else:
                tracker[board[i][column_num]] = 1
        return True

    def isCubeValid(self, cube: List[List[str]]) -> bool:
        starting_coords = []
        for i in range(0,9):
            for j in range(0,9):
                if i % 3 == 0 and j % 3 == 0:
                    starting_coords.append((i,j))
        print(starting_coords)
        for row, column in starting_coords:
            tracker = {}
            for i in range(0,3):
                for j in range(0,3):
                    print(row+i,column+j)
                    if cube[row+i][column+j] == ".":
                        next
                    elif cube[row+i][column+j] in tracker:
                        return False
                    else:
                        tracker[cube[row+i][column+j]] = 1
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        isAllRowsValid = True
        isAllColumnsValid = True
        for i in range(0, 9):
            isAllRowsValid = isAllRowsValid and self.isRowValid(board, i)
        for j in range(0,9):
            isAllColumnsValid = isAllColumnsValid and self.isColumnValid(board, j)
        return isAllRowsValid and isAllColumnsValid and self.isCubeValid(board)
        
        