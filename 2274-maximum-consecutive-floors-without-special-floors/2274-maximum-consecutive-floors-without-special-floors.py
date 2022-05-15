class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()
        maxSF = max(special[0]-bottom, top-special[-1])
        for i in range(1, len(special)):
            maxSF = max(special[i]-special[i-1]-1, maxSF)
        return maxSF