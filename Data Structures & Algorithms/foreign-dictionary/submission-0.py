class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        n = len(words)
        if n == 1:
            return words[0]
        indegrees={}
        visited={}
        res = []

        for word in words:
            for char in word:
                if char not in indegrees.keys():
                    indegrees[char]=set()
        
        for i in range(1,n):
            s,t= len(words[i-1]), len(words[i])
            for j in range(min(s,t)):
                if words[i-1][j]==words[i][j]:
                    continue
                elif words[i][j] in indegrees[words[i-1][j]]:
                    return ''
                else:
                    if words[i-1][j] not in indegrees[words[i][j]]:
                        indegrees[words[i][j]].add(words[i-1][j])
                    break
            if j==min(s,t)-1 and s>t:
                return ''
        
        def dfs(char):
            if char in visited:
                return visited[char]

            visited[char] = True

            for neighChar in indegrees[char]:
                if dfs(neighChar):
                    return True

            visited[char] = False
            res.append(char)

        for char in indegrees:
            if dfs(char):
                return ""

        # res.reverse()
        return "".join(res)



            