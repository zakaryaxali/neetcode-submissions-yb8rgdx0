class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 1. take 1 num as min
        # 2. check if mid <= min
        # 2a, if true take right half
        # 2b, if false take left
        # 3. iterate
        min_ = nums[0]
        n=len(nums)
        
        left=0
        right=n-1
        while left<right:
            mid = left + (right-left)//2
            if nums[mid]>=min_:
                left=mid+1
            else:
                min_=nums[mid]
                right=mid-1

        return min_