
VALUE = '=|=|=|='
class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs:
            return VALUE.join(strs)
        else:
            return ''

    def decode(self, s: str) -> List[str]:
        if s:
            return s.split(VALUE)
        else:
            return ['']
