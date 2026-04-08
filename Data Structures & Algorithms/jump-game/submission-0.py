class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 1 check len nums (if ==1 true)
        # 2 for each i check how far you can go and check where you land as long as it is not 0 unless last element
        # dfs where we check minimum jump then increase until we find at least one that works and return True 
        # else false
        n = len(nums)
        if n == 1:
            return True

        def dfs(i):
            # print(i)
            if i == n-1:
                return True
            if nums[i]==0:
                return False
            
            res = []
            for j in range(1,nums[i]+1):
                if i+j==n-1:
                        return True
                elif i+j<n-1: 
                    if dfs(i+j):
                        return True
                else:
                    break
            return False

        return dfs(0)