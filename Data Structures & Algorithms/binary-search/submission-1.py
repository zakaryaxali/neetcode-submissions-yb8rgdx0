class Solution:
    def search(self, nums: List[int], target: int, index=0) -> int:
        # print(nums)
        n = len(nums)
        if n == 0:
            return -1
        if n == 1:
            return index if target == nums[0] else -1

        if n % 2 == 0:
            half = int(n/2)
        else:
            half = int((n-1)/2)
        
        # print(half)
        if target == nums[half]:
            return index + half
        elif target > nums[half]:
            return self.search(nums[half+1:], target, index + half+1)
        else:
            return self.search(nums[:half], target, index)
        