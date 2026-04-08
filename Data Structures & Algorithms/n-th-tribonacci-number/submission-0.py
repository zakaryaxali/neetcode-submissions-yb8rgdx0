class Solution:
    def tribonacci(self, n: int) -> int:
        memo={}
        def dp(k):
            if k <= 0:
                return 0
            if k == 1:
                return 1
            if k == 2:
                return 1
            if k in memo.keys():
                return memo[k]
            
            memo[k]=dp(k-3)+dp(k-2)+dp(k-1)
            return memo[k]

        return dp(n)
        