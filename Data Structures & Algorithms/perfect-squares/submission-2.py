class Solution:
    def numSquares(self, n: int) -> int:
        squares=[]
        for i in range(n,0,-1):
            if i**2<=n:
                squares.append(i**2)
        # print(squares)
        min_ = math.inf

        def backtracking(curr,path):
            nonlocal min_
            if len(path)+1 < min_:
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