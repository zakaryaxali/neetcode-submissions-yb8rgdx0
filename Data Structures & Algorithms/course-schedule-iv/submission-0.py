class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        for p, c in prerequisites:
            adj[p].append(c)
        
        def dfs(current, visited, target):
            if current == target:
                return True
            if current in visited:
                return False
            visited.add(current)
            
            return any([dfs(course,visited,target) for course in adj[current]])
        result=[]
        for start, target in queries:
            result.append(dfs(start,set(),target))

        return result
