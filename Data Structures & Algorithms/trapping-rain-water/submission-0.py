class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n<=2:
            return 0
        
        left, right = 0, n - 1
        max_left = max_right = 0
        total = 0
        while left <= right:
            if max_left <= max_right:
                # update max_left
                max_left = max(max_left, height[left])
                # add water at left (what's the formula?)
                total+=max_left-height[left]
                # move left
                left+=1
            else:
                # mirror of the above
                max_right = max(max_right, height[right])
                total+=max_right-height[right]
                right-=1

        return total
        