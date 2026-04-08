class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap={}
        max_=0
        for num in nums:
            hashmap[num]=0
        for k in sorted(hashmap.keys()):
            if k-1 in hashmap.keys():
                hashmap[k]=hashmap[k-1]+1
            else:
                hashmap[k]=1
            if hashmap[k]>max_:
                max_=hashmap[k]

        return max_