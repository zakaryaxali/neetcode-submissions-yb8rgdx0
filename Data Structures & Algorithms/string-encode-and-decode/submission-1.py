
VALUE = '=|=|=|='
class Solution:

    def encode(self, strs: List[str]) -> str:
        return VALUE.join(strs)

    def decode(self, s: str) -> List[str]:
        return s.split(VALUE)
