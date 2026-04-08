class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.above=nums
        heapq.heapify(self.above)
        self.below = []
        heapq.heapify(self.below)
        self.k = k
        while len(self.above)>self.k:
            heapq.heappush(self.below, heapq.heappop(self.above))

    def add(self, val: int) -> int:
        heapq.heappush(self.above, val)
        while len(self.above)>self.k:
            heapq.heappush(self.below, heapq.heappop(self.above))
        return self.above[0] 
