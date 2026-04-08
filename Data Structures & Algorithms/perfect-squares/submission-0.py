class Solution:
    def numSquares(self, n: int) -> int:
        squares=[]
        for i in range(1,n+1):
            if i**2<=n:
                squares.append(i**2)
            else:
                break

        min_ = math.inf

        def backtracking(curr,path):
            nonlocal min_
            path.append(curr)
            if sum(path)==n:
                min_ =min(min_, len(path))
            elif sum(path)<n:
                for s in squares:
                    backtracking(s, path)
            path.pop()
            return

        for num in squares:
            backtracking(num,[])
        return min_