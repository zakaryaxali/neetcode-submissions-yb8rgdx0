class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        if n == 1:
            return 0

        def overlaps(starti, endi, startj, endj):
            if (starti<= startj and endi>=endj) or (startj<= starti and endj>=endi):
                return True
            if (starti< startj<endi) or (startj< starti < endj):
                return True
            if (starti< endj<endi) or (startj< endi < endj):
                return True
            return False    

        inorder = defaultdict(set)
        for i in range(n-1):
            starti, endi = intervals[i]
            for j in range(i+1,n):
                startj, endj = intervals[j]
                if overlaps(starti, endi, startj, endj):
                    inorder[i].add(j)
                    inorder[j].add(i)

        counter = 0
        seen=set()
        # temp = reversed(sorted(inorder.items(), key=lambda x: len(x[1])))
        # print([_ for _ in temp])
        for k,v in reversed(sorted(inorder.items(), key=lambda x: len(x[1]))):
            seen.add(k)
            for e in seen:
                v.discard(e)
            print(k,v)
            if len(v)>0:
                counter+=1

        return counter