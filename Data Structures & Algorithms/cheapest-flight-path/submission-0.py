class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #we could use bfs but we can optimize by using a modified version of dijkstra algo 
        # heap that will contain (current price, stop number, departure, arrival, current path?)
        # adj = hashmap of stop > [(price,arrival),...]
        # start with all the flights starting from src in heap
        # while heap?
        #   pop element 
        #   if arrival = dst > minprice = min(minprice, current price)
        #   else if stop number <k : add all non visited stops for this one to heap with current price += next price and stop number+=1
        # return minprice
        heap = []
        adj = defaultdict(list)
        minprice = math.inf
        for f,t,price in flights:
            adj[f].append((price,t))
        
        for price, t in adj[src]:
            heapq.heappush(heap, (price,0,src,t,[src,t]))
        
        while heap:
            currentprice, stops, f, t, path = heapq.heappop(heap)
            print(currentprice, stops, f, t, path)
            print(currentprice > minprice, stops > k, t == dst)
            if currentprice > minprice:
                continue
            if stops > k:
                continue
            if t == dst :
                print('test')
                minprice = min(minprice,currentprice)
                continue
            
            for price, nei in adj[t]:
                print(nei)
                if nei not in path:
                    path.append(nei)
                    heapq.heappush(heap, (currentprice+price,stops+1,t,nei,path[:]))
                    path.pop()

        return minprice if minprice!=math.inf else -1