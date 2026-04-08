class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        #we need to look for a pattern both present in str1 and st2 and that completes them both
        if len(str1)>len(str2):
            stra=str2
            strb = str1
        else:
            stra=str1
            strb=str2
        n=len(stra)
        i = n
        t = stra
        while i > 0:
            t = stra[:i]
            if not stra.replace(t,'') and not strb.replace(t,''):
                return t
            i-=1

        return ''
        