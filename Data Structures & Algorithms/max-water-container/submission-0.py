class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        start = 0
        end = n-1
        max_ = 0

        while start<end:
            area = min(heights[start],heights[end])*(end-start)
            max_ = max(max_, area)
            if heights[start] > heights[end]:
                end-=1
            else:
                start+=1

        return max_
