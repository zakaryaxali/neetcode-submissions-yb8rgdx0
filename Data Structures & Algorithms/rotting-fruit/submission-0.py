class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n==0:
            return -1
        m = len(grid[0])
        fresh=0
        minutes=0
        directions=[(1,0),(-1,0),(0,-1),(0,1),]
        queue=deque([])

        for r in range(n):
            for c in range(m):
                if grid[r][c]==2:
                    queue.append((r,c))
                if grid[r][c]==1:
                    fresh+=1

        while queue and fresh>0:
            minutes += 1
            for _ in range(len(queue)):
                r,c = queue.popleft()
                for dr,dc in directions:
                    if 0<=r+dr<n and 0<=c+dc<m:
                        if grid[r+dr][c+dc]==1:
                            fresh-=1
                            grid[r+dr][c+dc]=2
                            queue.append((r+dr,c+dc))

        return minutes if fresh==0 else -1
        