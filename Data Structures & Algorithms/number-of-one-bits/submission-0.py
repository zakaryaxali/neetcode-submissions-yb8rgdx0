class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        string = str(n)
        for i in range(32):
            count+=1 if string[i]==1 else 0
        return count