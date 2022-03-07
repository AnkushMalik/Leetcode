class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(sorted(arr),key=lambda d: bin(d)[2:].count('1'))