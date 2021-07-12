'''
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
'''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        val={}
        for i in range(len(s)):
            if s[i] in val:
                if val[s[i]]!=t[i]:
                    return False
            else:
                val[s[i]]=t[i]
        g=[]
        for key, value in val.items():
            if value in g:
                return False
            else:
                g.append(value)
                
        return True
        
