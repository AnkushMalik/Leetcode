class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1,len2 = len(word1),len(word2)
        n = min(len1,len2)
        ans = ''
        for i in range(n):
            ans+=word1[i]+word2[i]
        return ans+word1[n:]+word2[n:]