class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        n,m=len(grid),len(grid[0])
        directions=[(1,0),(-1,0),(0,1),(0,-1),]
        max_ = 0

        def dfs(i,j,counter):
            nonlocal visited
            nonlocal max_
            if (i,j) not in visited and grid[i][j]==1:
                counter+=1
                max_=max(max_,counter)
                visited.add((i,j))
                for dr,dc in directions:
                    if 0<=i+dr<n and 0<=j+dc<m:
                        dfs(i+dr,j+dc,counter)


        for i in range(n):
            for j in range(m):
                dfs(i,j,0)

        return max_
        