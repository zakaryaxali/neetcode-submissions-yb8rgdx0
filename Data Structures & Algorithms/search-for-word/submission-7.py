class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(1,0),(-1,0),(0,1),(0,-1),]
        n,m,s = len(board), len(board[0]), len(word)

        def dfs(i, row,col,visited):
            if (row,col) not in visited and 0<=row<n and 0<=col<m:
                if word[i]!=board[row][col]:
                    return False
                visited.add((row,col))
                if board[row][col]==word[i]:
                    if i+1<s:
                        for dr, dc in directions:
                            if dfs(i+1, row+dr, col+dc, visited):
                                return True
                    else:
                        return True
            return False

        for i in range(n):
            for j in range(m):
                if dfs(0,i,j,set()):
                    return True

        return False 