class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hsh = {}
        for i in strs:
            key = self.findHash(i)
            if key in hsh:
                hsh[key].append(i)
            else:
                hsh[key]=[i]
        return hsh.values()
    
    def findHash(self, s):
        hmap = [0]*26
        for i in s:
            hmap[ord(i)-ord('a')]+=1
        return str(hmap)