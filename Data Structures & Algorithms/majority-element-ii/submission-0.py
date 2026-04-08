class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counter = defaultdict(int)
        result=set()
        for num in nums:
            counter[num]+=1
            if counter[num]>n/3:
                result.add(num)

        return list(result)