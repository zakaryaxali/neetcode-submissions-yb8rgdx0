class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        result=[]
        index = 0
        if n > 0:
            current_interval = intervals[index]

        while index < n and current_interval[1]<newInterval[0]:
            result.append(current_interval)
            index+=1
            if index < n:
                current_interval = intervals[index]

        while index < n and current_interval[0]<=newInterval[1]:
            newInterval[0]=min(newInterval[0],current_interval[0])
            newInterval[1]=max(newInterval[1],current_interval[1])
            index+=1
            if index < n:
                current_interval = intervals[index]

        result.append(newInterval)

        while index<n:
            result.append(current_interval)
            index+=1
            if index < n:
                current_interval = intervals[index]

        return result
        