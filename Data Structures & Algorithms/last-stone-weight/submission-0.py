class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        result = [-stone for stone in stones]
        heapq.heapify(result)
        while len(result)>1:
            a=heapq.heappop(result)
            b=heapq.heappop(result)
            c=-abs(a-b)
            if not c==0:
                result.append(c)
        
        return -result[0] if len(result)==1 else 0
        