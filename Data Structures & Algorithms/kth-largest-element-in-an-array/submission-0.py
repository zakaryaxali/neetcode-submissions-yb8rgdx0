class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)
        i=0

        while i < k-1:
            heapq.heappop(nums)
            i+=1
        return -heapq.heappop(nums)      
        