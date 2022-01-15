class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        hp = []
        heapify(hp)
        intervals.sort(key=lambda x:x[0])
        heappush(hp,intervals.pop(0)[1])
        while intervals:
            newM = intervals.pop(0)
            if newM[0]>=hp[0]: heappop(hp)
            heappush(hp, newM[1])
        return len(hp)