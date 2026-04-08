class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        merged_list=[]
        i=0
        j=0
        while i<m and j<n:
            a = nums1[i]
            b = nums2[j]
            if a<b:
                merged_list.append(a)
                i+=1
            else:
                merged_list.append(b)
                j+=1
        merged_list += nums1[i:m]+nums2[j:n]
        for index, value in enumerate(merged_list):
            nums1[index]=value
        