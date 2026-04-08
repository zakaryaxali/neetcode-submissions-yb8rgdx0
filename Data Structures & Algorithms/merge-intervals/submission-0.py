class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        n = len(intervals)
        if n<2:
            return intervals
        intervals= sorted(intervals, key=lambda x: x[0])

        result = [intervals[0]]
        j=1
        # we want to check that next interval does not overlap with previous, other wise we merge
        while  j<n:
            prev_start, prev_end = result[-1]
            curr_start, curr_end = intervals[j]

            if prev_start <= curr_start <= prev_end:
                curr_start = prev_start
                if curr_end <= prev_end:
                    curr_end = prev_end
                result[-1] = [curr_start,curr_end]
            else:
                result.append([curr_start,curr_end])
            j+=1

        return result