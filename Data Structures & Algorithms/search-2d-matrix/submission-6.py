class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top_row, bottom_row = 0, ROWS - 1 

        # Binary search through rows 
        while top_row <= bottom_row:
            mid_row = (top_row + bottom_row) // 2
        
            # target is bigger than the biggest value in a current row
            if (target > matrix[mid_row][-1]):
                top_row = mid_row + 1
            
            # target is smaller than the smallest value in a current row
            elif (target < matrix[mid_row][0]):
                bottom_row = mid_row - 1

            else:
                # target value is in the current mid_row or we can't find the correct row
                # exit out of the loop
                break

        # if none of the rows contain the value
        if not (top_row <= bottom_row):
            return False

        # after narrow down the area (row) of the target value
        row = (top_row + bottom_row) // 2

        l, r = 0, COLS - 1

        # Perform a second binary search through the TARGET ROW
        while l <= r:
            m = (l + r) // 2

            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else: 
                return True

        return False