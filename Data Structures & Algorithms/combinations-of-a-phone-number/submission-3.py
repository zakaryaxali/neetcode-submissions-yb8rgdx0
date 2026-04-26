class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        hashmap = {
            2:'abc',
            3:'def',
            4:'ghi',
            5:'jkl',
            6:'mno',
            7:'pqrs',
            8:'tuv',
            9:'wxyz',
        }

        def dfs(digits, text):
            if not digits:
                return [text]
            digit = int(digits[0])
            res = []
            for char in hashmap[digit]:
                res.extend(dfs(digits[1:],text+char))

            return res

        return dfs(digits, '')