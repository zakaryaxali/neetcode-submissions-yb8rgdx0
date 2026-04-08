class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged=''
        i=0
        j=0
        k = 0
        while i<len(word1) and j<len(word2):
            if k == 0:
                merged+=word1[i]
                i+=1
            else:
                merged+=word2[j]
                j+=1
            k = (k + 1) % 2

        merged += word1[i:]+word2[j:]
        return merged
        