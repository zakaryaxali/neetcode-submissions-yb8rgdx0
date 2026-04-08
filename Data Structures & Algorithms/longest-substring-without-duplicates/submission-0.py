class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        start = 0
        end = 0
        max_ = 0
        positions = {}
        for c in s:
            if c in positions.keys(): 
                start = max(start, positions[c] + 1)
            
            max_ = max(max_, end-start+1)
            positions[c]= end
            end+=1
    
        return max_