class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort based on the first number 
        intervals.sort(key=lambda x: x[0])

        res = []
        
        # two pointers
        res.append(intervals[0])

        for i in intervals[1:]:
            temp = res.pop()
            if temp[0]<=i[0] and i[0] <= temp[1]:
                temp = [min(temp[0], i[0]), max(temp[1], i[1])]
                res.append(temp)
            else:
                res.append(temp)
                res.append(i)


        return res