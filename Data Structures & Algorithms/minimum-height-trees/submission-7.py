class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <=2:
            return [i for i in range(n)]
        adj = defaultdict(list)
        indegrees=[0]*n

        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
            indegrees[a]+=1
            indegrees[b]+=1

        queue = deque([])
        for i in range(n):
            if indegrees[i]==1:
                indegrees[i]-=1
                queue.append(i)

        nodes_left = n
        while nodes_left>2:
            leaves=len(queue)
            nodes_left-=leaves
            for _ in range(leaves):
                node = queue.popleft()
                for nei in adj:
                    if node in adj[nei]:
                        indegrees[nei]-=1
                        if indegrees[nei]==1:
                            queue.append(nei)
        
        return list(queue)
            