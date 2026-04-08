class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj=defaultdict(list)
        if len(edges) > (n - 1):
            return False

        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        seen=set()
        def dfs(node, par):
            if node in seen:
                return False

            seen.add(node)
            for nei in adj[node]:
                if nei == par:
                    continue
                if not dfs(nei, node):
                    return False
            return True

        return dfs(0, -1) and len(seen) == n
            