class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1: 
            return 1

        res=[[nums[0]]]
        for i in range(1,n):
            for arr in res:
                if nums[i] > arr[-1]:
                    temp = arr[:]
                    temp.append(nums[i])
                    if not temp in res:
                        res.append(temp)
            if not [nums[i]] in res:
                res.append([nums[i]])
        print (res)

        return max([len(arr) for arr in res])
