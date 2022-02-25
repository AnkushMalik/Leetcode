class Solution:
    def countOdds(self, low: int, high: int) -> int:
        diff = high-low
        return diff//2 if diff%2==0 and high%2==0 else diff//2+1