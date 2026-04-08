class Solution:
    def climbStairs(self, n: int) -> int:
        
        print(n)
        if n in result.keys():
            return result[n]
        
        result[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return result[n]