class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        remaining=defaultdict(int)
        cooldown=defaultdict(int)
        output=0
        
        for task in tasks:
            remaining[task]-=1
            cooldown[task]=0
        temp = [(v,k) for k,v in remaining.items()]
        heapq.heapify(temp)
        # print(temp)
        while temp:
            # we want to check at each turn if the task with most remaining element can be processed
            # if yes we do and we decrease remaining and we add cooldown
            # if not, we go to next task with hights remaining element
            # at the end of each turn each cooldown is decreased by one
            i=0
            output+=1
            m = len(temp)
            data=[]
            while i < m:
                r,task = heapq.heappop(temp)
                if cooldown[task]==0:
                    if r+1<0:
                        heapq.heappush(temp, (r+1, task))
                        cooldown[task]=n+1
                    i=m
                else:
                    data.append((r,task))
                i+=1
            for item in data:
                heapq.heappush(temp, item)
            for task in cooldown.keys():
                cooldown[task]=max(0,cooldown[task]-1)

        return output
        