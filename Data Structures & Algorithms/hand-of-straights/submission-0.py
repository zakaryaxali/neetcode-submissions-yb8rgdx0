class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hashmap=defaultdict(int)
        for num in hand:
            hashmap[num]+=1

        size = groupSize
        start = min(hand)
        for _ in range(len(hand)):
            # print(start, size)
            if start not in hashmap or hashmap[start]<0:
                return False
            else:
                hashmap[start]-=1
            size-=1
            if size==0:
                hashmap={k:v for k,v in hashmap.items() if v>0}
                # print(hashmap)
                if hashmap:
                    start = min(hashmap.keys())
                else:
                    break
                size=groupSize
            else:
                start+=1

        return size==0 and not hashmap