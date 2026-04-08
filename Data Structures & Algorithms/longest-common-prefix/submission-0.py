class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        j = 0
        prefix=''
        map = {}

        while j < len(strs[0]):
            map[j]=strs[0][j]

            for i in range(1, len(strs)):
                if j >= len(strs[i]) or strs[i][j] != map[j]:
                    return prefix

            prefix += map[j]
            j+=1


        return prefix