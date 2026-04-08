class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # we could use TrieNode here
        directions=[(1,0),(-1,0),(0,1),(0,-1),]
        m=len(board)
        n=len(board[0])
        res = set()
        max_size = len(words)
        words=set(words)
        def dfs(path, row,col,visited,word):
            nonlocal res
            if 0 <= row < m and 0 <= col <n and (row,col) not in visited:
                path += board[row][col] 
                if path == word:
                    res.add(path)
                elif path == word[:len(path)]:
                    visited.add((row,col))
                    for dr,dc in directions:
                        dfs(path,row+dr,col+dc,visited.copy(),word)


        for word in words:
            for row in range(m):
                for col in range(n):
                    dfs('',row,col,set(),word)
                    if word in res:
                        break
        return list(res)


