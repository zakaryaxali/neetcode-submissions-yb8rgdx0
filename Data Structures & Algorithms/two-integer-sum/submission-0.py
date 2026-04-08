class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {target-val:index for index, val in enumerate(nums)}

        for index, num in enumerate(nums):
            if num in map.keys() and map[num]!=index:
                return [index, map[num]]
        