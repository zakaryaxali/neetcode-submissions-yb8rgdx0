class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        duplicates = set()
        i=0
    
        while i < len(nums):
            if nums[i] in duplicates:
                return True
            else:
                duplicates.add(nums[i])
            i+=1
            if i > k:
                duplicates.remove(nums[i-k-1])

        return False
        