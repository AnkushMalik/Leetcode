class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        ts = []
        for trip in trips:
            ts.append([trip[1],trip[0]])
            ts.append([trip[2],-trip[0]])
        ts.sort()
        curr_pass = 0
        for time, passChange in ts:
            curr_pass += passChange
            if curr_pass>capacity:
                return False
        return True