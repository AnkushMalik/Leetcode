class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        maxscore = 0
        maxPoint = max(nums)
        hsh = [0] *(max(nums)+1)

        for i in nums: hsh[i]+=i
        
        @cache
        def findMaxScore(num):
            if num<2:
                return hsh[num]
            return max(findMaxScore(num-2)+hsh[num],findMaxScore(num-1))
        return findMaxScore(maxPoint)