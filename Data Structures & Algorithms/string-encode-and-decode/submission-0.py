
VALUE = '=|=|=|='
class Solution:

    def encode(self, strs: List[str]) -> str:
        VALUE.join(strs)

    def decode(self, s: str) -> List[str]:
        s.split(VALUE)
