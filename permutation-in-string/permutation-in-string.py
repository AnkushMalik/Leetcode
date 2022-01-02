class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1): return False
        s1map = [0]*26
        for i in s1:
            s1map[ord(i)-ord('a')]+=1
        
        for i in range(len(s2)-len(s1)+1):
            s2map = [0]*26
            for j in range(i,i+len(s1)):
                s2map[ord(s2[j])-ord('a')]+=1
            if s2map==s1map:
                return True
        return False