"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        n = len(intervals)
        if n < 2:
            return True

        intervals=sorted(intervals, key=lambda x: xstart)
        i=0
        j=1
        while j < n:
            if intervals[j].start<intervals[i].end:
                return False
            j+=1
            i+=1

        return True
