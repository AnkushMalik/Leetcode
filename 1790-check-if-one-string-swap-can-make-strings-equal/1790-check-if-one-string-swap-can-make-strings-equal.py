class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1==s2: return True
        def getMap(s):
            hsh = [0]*26
            for i in s:
                hsh[ord(i)-ord('a')]+=1
            return hsh
        map1 = getMap(s1)
        map2 = getMap(s2)
        if map1!=map2: return False
        diff =0
        for i in range(len(s1)):
            if s1[i]!=s2[i]: diff+=1
        if diff==0 or diff==2:
            return True
        return False