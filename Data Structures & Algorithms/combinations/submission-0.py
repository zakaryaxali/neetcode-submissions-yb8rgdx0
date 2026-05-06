class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def backtracking(path):
            if len(path)==k:
                result.append(path[:])
                return
            if path:
                start = path[-1]
            else:
                start=1
            for i in range(start, n+2-(k-len(path))):
                if i not in path:
                    path.append(i)
                    backtracking(path)
                    path.pop()

        backtracking([])
        return list(result)