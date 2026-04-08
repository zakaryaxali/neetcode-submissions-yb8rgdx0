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
            if word=='eaabcdgfa':
                print(path, word, visited, row,col)
            if 0 <= row < m and 0 <= col <n and (row,col) not in visited:
                path += board[row][col] 
                if path == word:
                    res.add(path)
                elif path == word[:len(path)]:
                    visited.add((row,col))
                    for dr,dc in directions:
                        dfs(path,row+dr,col+dc,visited.copy(),word)

        for row in range(m):
            for col in range(n):
                for word in words:
                    dfs('',row,col,set(),word)
                    if len(res)==max_size:
                        return list(res)
                for item in res:
                    words.discard(item)
        return list(res)


