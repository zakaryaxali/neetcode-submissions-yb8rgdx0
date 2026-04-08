class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        n = len(s)
        if n==1:
            return 1

        for char in s:
            hashmap[char]=0
        
        for char in hashmap.keys():
            left=0
            remaining=0
            for right in range(n):
                if s[right]!=char:
                    remaining+=1

                while remaining>k:
                    left+=1
                    if left >=n:
                        break
                    if not s[left]==char:
                        remaining-=1
                
                hashmap[char]=max(hashmap[char], right-left+1)

        print(hashmap)
        return max([val for val in hashmap.values()])
        