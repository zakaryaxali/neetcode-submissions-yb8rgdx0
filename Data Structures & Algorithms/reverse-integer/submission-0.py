class Solution:
    def reverse(self, x: int) -> int:
        is_negative = False
        if x < 0:
            x = -x 
            is_negative=True
        result = '-' if is_negative else ''
        result+=str(x)[::-1]
        result = int(result)
        if -2**31<= result <= 2**31 - 1:
            return result
        else:
            return 0
        