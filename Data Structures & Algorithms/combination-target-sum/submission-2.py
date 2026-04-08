class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # we use hashmap and check all possible frequency combinations then return them
        res= []
        n = len(nums)

        def backtracking(start,current_value,path):
            if current_value==target:
                res.append(path[:])
                return
            for i in range(start, n):
                num=nums[i]       
                current_value+=num
                if current_value<=target: 
                    path.append(num)
                    backtracking(i,current_value,path)
                    path.pop()
                current_value-=num

        backtracking(0, 0, [])
        return list(res)