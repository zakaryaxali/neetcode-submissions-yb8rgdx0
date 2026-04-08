class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        m = len(edges)
        if m < n-1:
            return n-m

        def not_seen(k,v, seen):
            temp = list(v) + [k]
            for item in temp:
                if item in seen:
                    return False
            return True

        res = defaultdict(set)
        for a , b in edges:
            res[a].add(b)
            for item in res[a]:
                res[b].add(item)
            res[b].add(a)
            for item in res[b]:
                res[a].add(item)
                
        counter = 0
        seen = set()
        for k,v in res.items():
            if len(v) < n-1 and not_seen(k,v,seen):
                print(k,v)
                counter+=1
                seen.update(v)
                seen.add(k)
        return counter