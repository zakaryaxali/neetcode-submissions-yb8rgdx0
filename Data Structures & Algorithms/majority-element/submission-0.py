class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        n = len(nums)

        for num in nums:
            counter[num] += 1
            if counter[num] > n//2:
                return num

        