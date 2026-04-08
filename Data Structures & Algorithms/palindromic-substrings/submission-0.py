class Solution:
    def countSubstrings(self, s: str) -> int:
        def is_palindrome(s):
            n = len(s)
            if n==1:
                return True
            i=0
            while i<n//2:
                if s[i]!=s[-i-1]:
                    return False
                i+=1
            return True
        counter=0
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                if is_palindrome(s[i:j]):
                    print(i,j, s[i:j])
                    counter+=1
        return counter   
        