class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <2:
            return nums
        
        i = 0
        j = 1

        while j<len(nums):
            if nums[j]==nums[i]:
                del nums[j]
            else:
                j+=1
                i+=1

        return len(nums)
