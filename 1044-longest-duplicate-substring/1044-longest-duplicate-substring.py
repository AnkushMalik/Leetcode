class Solution:
    def longestDupSubstring(self, s: str) -> str:
        ans = ''
        j = 1
        for i in range(len(s)-j+1):
            wd = s[i:i+j]
            while wd in s[i+1:]:
                ans = wd
                j+=1
                wd = s[i:i+j]
        return ans