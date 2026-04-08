class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        a = len(text1)
        b = len(text2)
        dp = [[0]*(b+1) for _ in range(a+1)]
        for row in reversed(range(a)):
            for col in reversed(range(b)):  
                if text2[col] == text1[row]:
                    dp[row][col] = 1 + dp[row + 1][col + 1]
                else:
                    dp[row][col] = max(dp[row + 1][col], dp[row][col + 1]) 
        
        return dp[0][0]
        