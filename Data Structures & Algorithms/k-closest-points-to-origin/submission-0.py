import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(point):
            return (point[0]**2)+(point[1]**2)

        # min heap
        res = []
        heapq.heapify(res)
        for point in points:
            dist = distance(point)
            heapq.heappush(res, (dist, point))

        final = []
        for i in range(k):
            dist, point = heapq.heappop(res)
            final.append(point)
        print(final)
        return final