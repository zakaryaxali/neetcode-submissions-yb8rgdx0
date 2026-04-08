class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n=min(len(s1),len(s2))
        m=max(len(s1),len(s2))
        if n==1:
            return s1 in s2 or s2 in s1

        (a,b)=(s1,s2) if len(s1)<len(s2) else (s2,s1)

        left = 0 
        right = n-1
        amap=defaultdict(int)
        bmap=defaultdict(int)
        for i in range(n):
            amap[a[i]]+=1
            bmap[b[i]]+=1

        while right<m:
            anagram = True
            for k,v in amap.items():
                if bmap[k]!=v:
                    anagram=False
                    break
            if anagram:
                return True
            else:
                right+=1
                if right==m:
                    break
                bmap[b[right]]+=1
                bmap[b[left]]-=1
                left+=1

        return False
