class MedianFinder:

    def __init__(self):
        self.upper = []
        self.lower = []
        heapq.heapify(self.lower)
        heapq.heapify(self.upper)

    def addNum(self, num: int) -> None:
        if not self.upper or num > self.upper[0]:
            heapq.heappush(self.upper,num)
        else:
            heapq.heappush(self.lower,-num)

        while len(self.upper)>len(self.lower)+1:
            data = heapq.heappop(self.upper)
            heapq.heappush(self.lower,-data)
        while len(self.lower)>len(self.upper):
            data = heapq.heappop(self.lower)
            heapq.heappush(self.upper,-data)


    def findMedian(self) -> float:
        if (len(self.upper)+len(self.lower))%2==0:
            return (self.upper[0]-self.lower[0])/2
        else:
            return self.upper[0]