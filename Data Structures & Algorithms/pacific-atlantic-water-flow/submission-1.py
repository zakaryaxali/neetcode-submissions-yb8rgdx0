class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions=[(1,0),(-1,0),(0,-1),(0,1),]
        n,m = len(heights), len(heights[0])
        pacific = {}
        atlantic = {}
        visited = set()
        for i in range(n):
            pacific[(i,0)]=True
            atlantic[(i,m-1)]=True
        for i in range(m):
            pacific[(0,i)]=True
            atlantic[(n-1,i)]=True

        def dfs(i,j, is_atlantic):
            ocean = atlantic if is_atlantic else pacific

            if (i,j) not in ocean.keys():
            
                ocean[(i,j)]=False

                for dr, dc in directions:
                    if 0<= i + dr < n and 0<= j+dc<m and heights[i][j]>= heights[i+dr][j+dc]:
                        if dfs(i+dr,j+dc, is_atlantic):
                            ocean[(i,j)]=True
                            break
            
            return ocean[(i,j)]


        res = []
        for i in range(n):
            for j in range(m):
                dfs(i,j, True)
                dfs(i,j, False)
                if atlantic[(i,j)] and pacific[(i,j)]:
                    res.append([i,j])

        return res
        
