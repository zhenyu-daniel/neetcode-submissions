"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
            starting = 1
            intervals.sort(key=lambda i: i.start)
            while starting<len(intervals) and True:
                if (intervals[starting].start<=intervals[starting-1].start) or (intervals[starting].start<intervals[starting-1].end):
                    return False
                starting += 1

            return True

                