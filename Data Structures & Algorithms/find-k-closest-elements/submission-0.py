class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(points) < k:
            return points
        distances = [(x**2 + y**2, [x,y]) for x,y in points]
        heapq.heapify(distances)
        i = 0
        result = []

        while i < k:
            i+=1
            point = heapq.heappop(distances)[1]
            result.append(point)

        return result

        