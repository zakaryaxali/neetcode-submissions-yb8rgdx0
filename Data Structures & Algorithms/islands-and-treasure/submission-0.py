class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n,m = len(grid),len(grid[0])
        directions = [(1,0),(-1,0),(0,-1),(0,1),]
        seen = set()

        def get_dist(c,r,dist):
            if 0 <= r< n and 0 <= c < m: 
                if grid[r][c] in [-1,0] or grid[r][c]<=dist:
                    return
                else:
                    grid[r][c] = dist
                    for dr,dc in directions:
                        get_dist(r+dr,c+dc,path+1)

        for r in range(n):
            for c in range(m):
                if grid[r][c]==0:
                    # see
                    for dr,dc in directions:
                        get_dist(r+dr,c+dc,1)
                    
            