class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        sys.setrecursionlimit(20000)
        memo = {}
        n=len(s)

        def backtracking(i):
            # print(i,j,memo)
            if i in memo:
                return memo[i]
            if i == n-1:
                return True
            for j in range(i+minJump,min(i+maxJump,n-1)+1):
                if s[j]=='0' and backtracking(j):
                    result = True
                    break
            else:
                result = False

            memo[i]=result
            # print(i,j,result)
            return result
        
        return backtracking(0)
