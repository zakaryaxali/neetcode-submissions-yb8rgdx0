class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []

        def backtracking(val, combinations):
            if val not in combinations:
                combinations.append(val)
            else:
                return
            if len(combinations)==n:
                result.append(combinations[:])
                return
            else:
                for i in range(n):
                    backtracking(nums[i],combinations[:])
            return 
        
        for i in range(n):
            backtracking(nums[i], [])
        return result
        