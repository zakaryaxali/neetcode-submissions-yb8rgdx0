class Solution:
    def _init_(self):
        self.count = 0
        self.graphs = []
        self.groups = {}

    def merge(self, a, b):
        tmp = self.graphs[groups[a]]
        self.groups[a]=self.groups[b]
        for item in tmp:
            self.graphs[groups[a]].add(item)
            self.groups[item]=self.groups[b]


    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        graphs = []
        groups = {}

        def merge(a, b):
            tmp = graphs[groups[a]]
            groups[a]=groups[b]
            for item in tmp:
                graphs[groups[a]].add(item)
                groups[item]=groups[b]
        m = len(edges)
        count = n
        for a , b in edges:
            if a not in groups.keys() and b not in groups.keys():
                graphs.append([a,b])
                groups[a] = groups[b] = len(graphs)-1
                count-=1
            elif a in groups.keys() and b not in groups.keys():                
                groups[b] = groups[a]
                graphs[groups[a]].append(b)
                count-=1
            elif a not in groups.keys() and b in groups.keys():                
                groups[a] = groups[b]
                graphs[groups[a]].append(a)
                count-=1
            elif groups[b] != groups[a]:
                merge(a,b)
                count-=1
                

        return count


        