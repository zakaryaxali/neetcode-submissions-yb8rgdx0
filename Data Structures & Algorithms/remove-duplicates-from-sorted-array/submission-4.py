class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp = set()
        for num in nums:
            if num not in temp:
                temp.add(num)
        
        nums = list(temp)
        return len(nums)