class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n==1:
            return s
        
        max_ = 1
        res = ''

        def is_palindrome(i , left, right):
            nonlocal max_
            nonlocal res
            if 0<=i+left and i+right<n:
                if s[i+left]==s[i+right]:
                    if max_ < right-left+1:
                        max_=right-left+1
                        res = s[i+left:i+right+1]
                    is_palindrome(i , left-1, right+1)

        for i in range(n):
            is_palindrome(i,-1,1)
            if i<n-1 and s[i]==s[i+1]:
                # print(max_, s[i:i+2])
                if max_ < 2:
                    max_=2
                    res = s[i:i+2]
                is_palindrome(i,-1,2)

        return res