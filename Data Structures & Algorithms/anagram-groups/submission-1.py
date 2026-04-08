class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        n = len(strs)
        if n == 1:
            return [strs]

        def is_anagram(a, b):
            if len(a)!=len(b):
                return False
            i=0
            while i < len(a):
                b = b.replace(a[i],'',1)
                if len(b)!=len(a)-i-1:
                    return False
                i+=1
            return True

        seen = set()
        
        for i in range(n):
            if not i in seen:
                seen.add(i)
                group = [strs[i]]
                for j in range(i+1,n):
                    if not j in seen and is_anagram(strs[i],strs[j]):
                        print(i,j)
                        seen.add(j)
                        group.append(strs[j])
                result.append(group)

        return result
    