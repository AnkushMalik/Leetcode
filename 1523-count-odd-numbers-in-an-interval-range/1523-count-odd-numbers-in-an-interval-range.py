class Solution:
    def countOdds(self, low: int, high: int) -> int:
        diff = high-low
        if diff%2==0:
            if high%2==0:
                return diff//2
            else:
                return diff//2+1
        return diff//2+1