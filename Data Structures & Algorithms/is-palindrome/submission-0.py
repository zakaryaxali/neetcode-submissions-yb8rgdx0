class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()
        s = [_ for _ in s if _.isalnum()]
        # print(s)
        i = 0 
        j = len(s)-1
        while i<j:
            if not s[i] == s[j]:
                return False
            i+=1
            j-=1
        return True