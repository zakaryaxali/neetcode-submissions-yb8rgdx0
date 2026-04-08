class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)

        for num in nums:
            hashmap[num]+=1
        
        temp = [(-v,k) for k,v in hashmap.items()]
        heapq.heapify(temp)

        i = 0
        result = []
        while i < k:
            result.append(heapq.heappop(temp)[1])
            i+=1

        return result