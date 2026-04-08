class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        result=[]
        n = len(nums)

        def list_xor(nums):
            n = len(nums)
            res=0
            if n:
                res=nums[0]
                for i in range(1,n):
                    res^=nums[i]
            return res
        print(nums[1:2])
        for i in range(n):
            for j in range(i+1,n+1):
                result.append(list_xor(nums[i:j]))
        
        return sum(result)