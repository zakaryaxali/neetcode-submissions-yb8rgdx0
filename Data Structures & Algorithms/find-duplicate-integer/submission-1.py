class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        i = 0
        j = 2

        while True:
            if nums[i%n]==nums[j%n]:
                return nums[i%n]
            i+=1
            j+=2

        # return res
        