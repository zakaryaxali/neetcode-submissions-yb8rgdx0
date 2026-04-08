class Solution:
    def minEnd(self, n: int, x: int) -> int:
        i = x
        arr = []
        while n:
            if i & x == x:
                # print(i)
                arr.append(i)
                n-=1
            i+=1
        
        return arr[-1]
