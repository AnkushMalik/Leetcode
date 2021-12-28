# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        j = n
        while i<=j:
            mid = (i+j)//2
            midchk = isBadVersion(mid)
            midleftchk = isBadVersion(mid-1)
            if midchk:
                j = mid-1
                if midleftchk == False:
                    return mid
            else:
                i = mid+1
        return mid