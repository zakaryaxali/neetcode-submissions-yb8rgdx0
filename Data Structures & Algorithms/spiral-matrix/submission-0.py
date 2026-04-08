class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        visited=set()
        visited.add((0,0))
        result = [matrix[0][0]]
        i,j=0,0
        while len(visited)<n*m:
            for dr,dc in directions:
                # print('outer', dr,dc )
                while 0 <= i + dr < n and 0 <= j + dc < m and (i+dr,j+dc) not in visited:
                    # print('inner', i+dr,j +dc)
                    result.append(matrix[i+dr][j+dc])
                    visited.add((i+dr,j+dc))
                    i+=dr
                    j+=dc

        return result
        