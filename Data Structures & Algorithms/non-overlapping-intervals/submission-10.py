class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])

        pre = intervals[0]
        counter = 0

        for i in intervals[1:]:
            if i[0] >= pre[1]:
                pre = i
                continue
            else:
                counter += 1
                if i[1] < pre[1]:
                    pre = i

        return counter