class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n = len(heights)
        m = len(heights[0])
        if n==1 and m==1:
            return 0

        heap = [(0,0,0)]
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        visited = set()
        while heap:
            effort, row, col = heapq.heappop(heap)
            if (row,col) in visited:
                continue
            visited.add((row,col))
            if row==n-1 and col==m-1:
                return effort
            
            for dr,dc in dirs:
                nr,nc = row+dr, col+dc
                if 0<=nr<n and 0<=nc<m and (nr,nc) not in visited:
                    new_effort = max(effort, abs(heights[row][col]-heights[nr][nc]))
                    heapq.heappush(heap, (new_effort, nr,nc))

        return 0
