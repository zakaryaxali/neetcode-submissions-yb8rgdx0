class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        i = n-1
        carry = 1
        while i >= 0:
            if digits[i]==9 and carry == 1:
                digits[i]=0
                carry = 1
            elif carry == 1:
                digits[i]+=1
                carry=0
                break
            i-=1
        if carry ==1:
            digits.append(0)
            digits[0]=1

        return digits
        