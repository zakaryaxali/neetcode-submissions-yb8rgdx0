class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        map = {i:[False, 0] for i in range(1,n+1)}

        for person, trustee in trust:
            map[person][0]=True
            map[trustee][1]+=1

        for k,v in map.items():
            if not v[0] and v[1]==n-1:
                return k
        
        return -1