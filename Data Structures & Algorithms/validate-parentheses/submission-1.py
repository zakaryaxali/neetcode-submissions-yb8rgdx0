class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets=[]

        for i in range(len(s)):
            if s[i]==']':
                if open_brackets and open_brackets[-1] == '[':
                    del open_brackets[-1]
                else:
                    return False
            elif s[i]=='}':
                if open_brackets and open_brackets[-1] == '{':
                    del open_brackets[-1]
                else:
                    return False
            elif s[i]==')':
                if open_brackets and open_brackets[-1] == '(':
                    del open_brackets[-1]
                else:
                    return False
            else:
                open_brackets.append(s[i])


        return not len(open_brackets)

        