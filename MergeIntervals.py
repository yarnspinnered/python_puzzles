# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return []

        intervals.sort(key = lambda x: x.start)
        currInterv = intervals[0]
        results = []

        for interv in intervals[1:]:
            if interv.start <= currInterv.end:
                currInterv.end = max(currInterv.end, interv.end)
            else:
                results.append(currInterv)
                currInterv = interv
        results.append(currInterv)

        return results