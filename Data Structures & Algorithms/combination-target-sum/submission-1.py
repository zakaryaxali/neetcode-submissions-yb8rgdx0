class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # we use hashmap and check all possible frequency combinations then return them
        hashmap={}
        res= []
        n = len(nums)
        if n==1:
            if target==nums[0]:
                return [target]
            else:
                return []
        for num in nums:
            hashmap[num]=0

        def get_sum(combination):
            return sum([k*v for k,v in combination.items()])

        def dfs(combination):
            for key in combination.keys():
                combination[key]+=1
                total = get_sum(combination)
                if total == target:
                    path = []
                    for k,v in combination.items():
                        path.extend([k]*v)
                    # print(path)
                    if path not in res:
                        res.append(path)
                elif total < target:
                    dfs(combination.copy())

                
                combination[key]-=1

        dfs(hashmap)
        return list(res)