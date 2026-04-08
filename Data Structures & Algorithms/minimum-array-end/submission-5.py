class Solution:
    def minEnd(self, n: int, x: int) -> int:
        i = min(x,n)
        # arr = []
        while n:
            if i & x == x:
                # arr.append(i)
                n-=1
            i+=1
        
        return i-1
