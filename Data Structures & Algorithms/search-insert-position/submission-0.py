class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 1:
            return 1 if target > nums[0] else 0

        left=0
        right=n-1
        while left <=right:
            pivot = left + (right-left)//2
            if nums[pivot]==target:
                return pivot
            elif nums[pivot]> target:
                right=pivot-1
            else:
                left=pivot+1

        return left
        
        