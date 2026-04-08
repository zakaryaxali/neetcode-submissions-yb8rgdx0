
VALUE = '=|=|=|='
class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs:
            return VALUE.join(strs)
        else:
            return ''

    def decode(self, s: str) -> List[str]:
        if s is not None and s != '' :
            print(s,'l')
            return s.split(VALUE)
        else:
            return []
