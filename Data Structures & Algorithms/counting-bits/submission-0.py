class Solution:
    def countBits(self, n: int) -> List[int]:
        if n ==0 :
            return []
        
        def count_bits(i):
            one=0
            for j in range(32):
                if i & (1 <<j):
                    one+=1
            return one

        result = [0]*(n+1)
        
        for i in range(1,n+1):
            result[i]=count_bits(i)

        return result