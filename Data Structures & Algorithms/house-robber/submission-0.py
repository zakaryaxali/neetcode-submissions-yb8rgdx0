class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        
        def rob_helper(start: int) -> int:
            if start in cache:
                return cache[start]
            
            if start >= len(nums):
                return 0
            if start == len(nums) - 1:
                return nums[start]
            
            option_a = nums[start] + rob_helper(start + 2)
            option_b = rob_helper(start + 1)
            
            cache[start] = max(option_a, option_b)
            return cache[start]
        
        return rob_helper(0)
        