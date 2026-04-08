class Solution:
    def romanToInt(self, s: str) -> int:
        n = len(s)
        dictionary = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900,
        }
        i = 0
        result=0
        
        while i < n-1:
            if s[i] in dictionary.keys() and f'{s[i]}{s[i+1]}' in  dictionary.keys():
                result+=dictionary[f'{s[i]}{s[i+1]}']
                i+=2
            else:
                result+=dictionary[s[i]]
                i+=1


        if i<n:
            result+=dictionary[s[i]]
        
        return result
        