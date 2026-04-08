class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        for start in range(n):
            current_gas=gas[start]
            complete=True
            for j in range(n):
                current_gas-=cost[(j+start)%n]
                if current_gas<0:
                    complete =False
                    break
                else:
                    current_gas+=gas[(j+start+1)%n]
            if complete:
                return start
        return -1