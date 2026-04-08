class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[0]*n
        dp[0]=nums[0]

        for i in range(1,n):
            dp[i]=1+dp[i-1] if nums[i] else 0

        return max(dp)