class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        hsh = {}
        maxs = 0
        currmax = 0
        while i<len(s):
            if s[i] in hsh:
                i = hsh[s[i]]+1
                hsh = {}
                currmax = 0
            else:
                hsh[s[i]]=i
                currmax+=1
                maxs = max(maxs,currmax)
                i+=1
        return maxs