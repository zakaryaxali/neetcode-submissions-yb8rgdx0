class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ordermap = {order[i]:i for i in range(len(order))}
        
        n=len(words)

        for i in range(n-1):
            wordi = words[i]
            for j in range(i+1,n):
                wordj=words[j]
                sameletter=True
                for k in range(min(len(wordi),len(wordj))):
                    if ordermap[wordi[k]]>ordermap[wordj[k]]:
                        return False
                    if ordermap[wordj[k]]>ordermap[wordi[k]]:
                        sameletter=False
                        break
                
                if k == len(wordj)-1 and sameletter and len(wordi)>len(wordj):
                    return False
                
        return True