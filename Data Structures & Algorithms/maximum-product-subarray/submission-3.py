class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp=[[nums[0], nums[0]]]
        for i in range(1, n):
            temp = dp[i-1][0]*nums[i],nums[i],dp[i-1][1]*nums[i]
            dp.append([max(temp), min(temp)])

        print(dp)
        return max([x[0] for x in dp])