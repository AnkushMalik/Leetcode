class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_ord, t_ord = 0, 0
        for ss in s:
         s_ord += ord(ss)
        for tt in t:
         t_ord += ord(tt)

        return chr(t_ord - s_ord)