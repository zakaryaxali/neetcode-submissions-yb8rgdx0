class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # min_ = max(piles)

        def is_valid(bph):
            time = 0
            for pile in piles:
                time+=pile//bph
                time+=0 if pile%bph==0 else 1
                if time>h:
                    return False
            return True


        left = 1
        right = max(piles)
        result = -1

        while left <= right:
            mid = (left + right) // 2
            
            # If the middle element is True, it could be the first occurrence.
            # Store the index and search the left half to find an earlier one.
            if is_valid(mid) == True:
                result = mid
                right = mid - 1 # Search left
            
            # If the middle element is False, the first True must be in the right half.
            else:
                left = mid + 1

        return result