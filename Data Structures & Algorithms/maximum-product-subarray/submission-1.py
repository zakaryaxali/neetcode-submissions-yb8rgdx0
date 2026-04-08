class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-math.inf]*(n)
        dp[0]=max(dp[0], nums[0])
        for i in range(1, n):
            dp[i]=max(dp[i-1]*nums[i],nums[i],nums[i-1]*nums[i])

        return max(dp)