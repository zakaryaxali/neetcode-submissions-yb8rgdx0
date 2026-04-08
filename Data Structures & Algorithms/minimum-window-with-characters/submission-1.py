class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 1. check all t letter are in s
        # 2. if so, create sliding window of inscreasing size
        n = len(s)
        m = len(t)
        if m > n:
            return ''

        for char in t:
            if char not in s:
                return ''
        if m==n:
            return s
        if m ==1:
            return t

        k = m
        
        while k<=n:
            for i in range(n-k):
                is_min = True
                for char in t:
                    if char not in s[i:k+i+1]:
                        is_min = False
                        break
                if is_min:
                    return s[i:k+i+1]
                
            k+=1
        
        return ''


