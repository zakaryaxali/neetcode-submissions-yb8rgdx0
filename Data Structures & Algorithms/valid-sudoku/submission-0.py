class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        v = {i:set() for i in range(n)}
        h = {i:set() for i in range(n)}
        s = {i:{j:set() for j in range(3)} for i in range(3)}
        for i in range(n):
            for j in range(n):
                if board[i][j].isdigit():
                    num = int(board[i][j])
                    if num in v[j] or num in h[i] or num in s[i//3][j//3]:
                        return False
                    else:
                        v[j].add(num)
                        h[i].add(num)
                        s[i//3][j//3].add(num)

        return True