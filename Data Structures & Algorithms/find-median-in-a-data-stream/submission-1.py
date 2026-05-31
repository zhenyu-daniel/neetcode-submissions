from heapq import *
class MedianFinder:

    def __init__(self):
        self.small, self.big = [], []
        # small is max heap
        # big is min heap
        # python only has min heap
    def addNum(self, num: int) -> None:
        heappush(self.small, -1*num)

        # first condition: is val in small < val in big heap
        if self.small and self.big and (-1*self.small[0] > self.big[0]):
            heappush(self.big, -1*self.small[0])
            heappop(self.small)

        # check the length
        if len(self.small) - len(self.big) >1:
            heappush(self.big, -1*self.small[0])
            heappop(self.small)
        if len(self.big) - len(self.small) >1:
            heappush(self.small, -1*self.big[0])
            heappop(self.big)

    def findMedian(self) -> float:
        if len(self.small) > len(self.big):
            return -1*self.small[0]
        elif len(self.small) == len(self.big):
            return (-1*self.small[0]+self.big[0]) / 2
        else:
            return self.big[0]
        
        