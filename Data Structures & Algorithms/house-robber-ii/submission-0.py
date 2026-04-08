class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return max(nums)

        def dp(nums):
            n = len(nums)
            if n <= 1:
                return max(nums)

            dp = [0]*(n)
            dp[0]=nums[0]
            dp[1]=max(nums[1],nums[0])
            for i in range(2,n):
                dp[i]=max(dp[i-1],nums[i]+dp[i-2])

            return dp[-1]

        return max(dp(nums[:-1]),dp(nums[1:]))