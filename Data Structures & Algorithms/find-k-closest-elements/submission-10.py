class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) < k:
            return arr
        distances = [(abs(x-y),y) for y in arr]
        heapq.heapify(distances)
        i = 0
        result = []

        while i < k:
            i+=1
            point = heapq.heappop(distances)[1]
            result.append(point)

        return result