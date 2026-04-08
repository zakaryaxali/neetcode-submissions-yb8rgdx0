class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 1. check all t letter are in s
        # 2. if so, create sliding window of inscreasing size
        n = len(s)
        m = len(t)
        if m > n:
            return ''

        tmap=defaultdict(int)
        smap=defaultdict(int)
        for char in s:
            smap[char]+=1
        for char in t:
            tmap[char]+=1
            
        for k,v in tmap.items():
            if k not in smap.keys() or smap[k]<tmap[k]:
                return ''

        if m==n:
            return s
        if m ==1:
            return t

        j = m
        
        while j<=n:
            for i in range(n-j+1):
                temp=defaultdict(int)
                for char in s[i:j+i]:
                    temp[char]+=1
                
                is_min = True
                for k,v in tmap.items():
                    if k not in temp.keys() or temp[k]<tmap[k]:
                        is_min = False
                        break
                if is_min:
                    return s[i:j+i]
                
            j+=1
        
        return ''


