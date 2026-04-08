class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        taken = 0
        graph = defaultdict(list)
        indegrees = [0]*numCourses

        for dest, src in prerequisites:
            graph[src].append(dest)
            indegrees[dest]+=1

        queue = deque([i for i in range(numCourses) if indegrees[i]==0])

        while queue:
            c = queue.pop()
            for d in graph[c]:
                indegrees[d]-=1
                if indegrees[d]==0:
                    queue.append(d)
            taken+=1

        return taken==numCourses
        