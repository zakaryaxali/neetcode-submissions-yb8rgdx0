class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        result=0

        def backtracking(i,current_sum):
            nonlocal result
            suma=current_sum+nums[i]
            sumb=current_sum-nums[i]
            if i ==n-1:
                if suma == target:
                    result+=1
                if sumb == target:
                    result+=1
                return
            backtracking(i+1,suma)
            backtracking(i+1,sumb)

        backtracking(0,0)
        return result