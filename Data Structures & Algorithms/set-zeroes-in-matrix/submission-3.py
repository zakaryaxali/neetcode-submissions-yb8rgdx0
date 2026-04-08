class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n,m=len(matrix),len(matrix[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1),]
        seen = set()
        def dfs(r,c,dr,dc):
            if 0<=r<n and 0<=c<m and matrix[r][c]!= 0 and not (r,c) in seen:
                seen.add((r,c))
                matrix[r][c]=0
                dfs(r+dr,c+dc,dr,dc)
            return
 
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0 and not (i,j) in seen:
                    seen.add((i,j))
                    print(i,j)
                    for dr,dc in directions:
                        dfs(i+dr,j+dc,dr,dc)

        return
        