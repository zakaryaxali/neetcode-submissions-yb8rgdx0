class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        n,m = len(grid), len(grid[0])
        res = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    for dr,dc in directions:
                        if i+dr<0 or i+dr>=n or j+dc<0 or j+dc>=m or grid[i+dr][j+dc]==0:
                            res+=1
        return res