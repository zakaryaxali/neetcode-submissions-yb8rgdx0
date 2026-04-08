class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*(n)
        dp[0]=max(1, nums[0])
        for i in range(1, n):
            dp[i]=max(dp[i-1]*nums[i],nums[i],nums[i-1]*nums[i])

        return max(dp)