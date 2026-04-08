class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n=len(s1)
        m=len(s2)
        if n==1:
            return s1 in s2
        if m < n:
            return False

        left = 0 
        right = n-1
        s1map=defaultdict(int)
        s2map=defaultdict(int)
        for i in range(n):
            s1map[s1[i]]+=1
            s2map[s2[i]]+=1

        while right<m:
            anagram = True
            for k,v in s1map.items():
                if s2map[k]!=v:
                    anagram=False
                    break
            if anagram:
                return True
            else:
                right+=1
                if right==m:
                    break
                s2map[s2[right]]+=1
                s2map[s2[left]]-=1
                left+=1

        return False
