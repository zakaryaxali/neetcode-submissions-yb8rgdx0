class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n,m=len(matrix),len(matrix[0])
        def get_coordinates(i):
            # turn one integer into 2 (row and col)
            row = i // m
            col = i % m
            return row, col

        left = 0
        right = m*n-1

        while left<=right:
            mid = left + (right-left)//2
            r,c = get_coordinates(mid)
            print(r,c,mid)
            if matrix[r][c]==target:
                return True
            elif matrix[r][c]>target:
                right=mid-1
            else:
                left = mid+1

        return False