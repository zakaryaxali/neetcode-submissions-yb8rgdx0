class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        def dp(start):
            if start in cache.keys():
                return cache[start]
            if start >= len(cost)-1:
                return 0
            
            option_b = cost[start] + dp(start+1)
            option_a = cost[start+1] + dp(start+2)
            
            cache[start]=min(option_a,option_b)
            return cache[start]
        
        
        return dp(0)
        