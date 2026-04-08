class Solution:
    def minEnd(self, n: int, x: int) -> int:
        def is_bit(i,x,arr):
            ans = x
            for num in arr:
                ans &= num
                if not ans == x:
                    return False

            return ans & i == x

        i = x
        arr = []
        while n and i<100:
            if is_bit(i,x,arr):
                print(i)
                arr.append(i)
                n-=1
            i+=1
        
        return arr[-1]
