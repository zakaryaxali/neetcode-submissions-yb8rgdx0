class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        counter = 0
        directions= [(1,0),(-1,0),(0,1),(0,-1)]

        def dfs(row, col):
            if 0 <= row < n and 0 <= col < m and grid[row][col] == "1" :
                grid[row][col]="0"
                for dr,dc in directions:
                    dfs(row+dr, col+dc)
                    
        for r in range(n): 
            for c in range(m):
                if grid[r][c]=="1":
                    dfs(r,c)
                    counter+=1
        return counter
        