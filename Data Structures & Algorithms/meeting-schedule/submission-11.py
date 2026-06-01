"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x: x.start)

        if not intervals:
            return True
        
        if len(intervals) == 1:
            return True

        l, r = 0, 1

        while l<r and r<=len(intervals)-1:
            if intervals[r].start < intervals[l].end:
                return False
            else:
                l = r
                r += 1




        return True