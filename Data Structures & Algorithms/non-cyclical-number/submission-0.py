class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        result = n
        while result not in seen:
            seen.add(result)
            string = str(result)
            result = 0
            for char in string:
                result+=int(char)**2
            if result == 1:
                return True
        return False
        