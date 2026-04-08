class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not len(s) == len(t):
            return False
        
        anagram = defaultdict(int)

        for i in range(len(s)):
            anagram[s[i]] +=1
            anagram[t[i]] -=1

        for _, value in anagram.items():
            if value !=0:
                return False

        return True
        