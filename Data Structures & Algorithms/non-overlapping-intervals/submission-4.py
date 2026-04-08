class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])  # sort by end time
        
        removals = 0
        prev_end = intervals[0][1]
        
        for start, end in intervals[1:]:
            if start < prev_end:
                # Overlap: remove the one with later end (current one, since sorted)
                removals += 1
                # prev_end stays the same (we keep the earlier-ending interval)
            else:
                # No overlap: move prev_end forward
                prev_end = end
        
        return removals