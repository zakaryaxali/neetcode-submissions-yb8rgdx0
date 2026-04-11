from typing import List


class Solution:
    def get_merges(self, corpus: str, num_merges: int) -> List[List[str]]:
        # 1. Split corpus into a list of individual characters
        # 2. For each merge step:
        #    a. Count frequency of all adjacent token pairs
        #    b. Find the most frequent pair (break ties lexicographically)
        #    c. Merge all non-overlapping occurrences left to right
        #    d. Record the merge as [token_a, token_b]
        # 3. Return the list of merges performed
        temp = list(corpus)
        res = []
        for i in range(num_merges):
            couples = defaultdict(int)
            for j in range(1, len(temp)):
                couples[(temp[j-1],temp[j])]+=1

            best_count = max(couples.values())
            candidates = sorted(p for p, c in couples.items() if c == best_count)
            best = candidates[0]
            
            
            res.append(best)
            old = temp
            temp = []
            j=1
            while j < len(old):
                if old[j-1]==best[0] and old[j]==best[1]:
                    temp.append(best[0]+best[1])
                    j+=2
                else:
                    temp.append(old[j-1])
                    j+=1
            if j==len(old):
                temp.append(old[j-1])
            
            # print(temp)

        return res 
