class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums=[]

        for token in tokens:
            if token == '+':
                a = nums.pop()
                b = nums.pop()
                nums.append(a+b)
            elif token == '-':
                a = nums.pop()
                b = nums.pop()
                nums.append(b-a)
            elif token == '*':
                a = nums.pop()
                b = nums.pop()
                nums.append(a*b)
            elif token == '/':
                a = nums.pop()
                b = nums.pop()
                nums.append(int(b/a))
            else:
                nums.append(int(token))
        
        return nums.pop()
        