'''
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
Example 4:

Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"
'''
class Solution:
    def decodeString(self, s: str) -> str:
        if len(s)<=1: return s
        
        outerShells = [] #keep track of outer shells indices
        shellMatcher = [] #stack to push symbols
        osOpen = 0
        
        for i in range(len(s)):
            if s[i]=='[':
                shellMatcher.append('[')
                if osOpen == 0: #isEmpty? first osOpen
                    osOpen = i
            elif s[i]==']':
                shellMatcher.pop()
                if len(shellMatcher)==0:
                    outerShells.append((osOpen,i))
                    osOpen=0
        
        if not outerShells: return s
        idxAdder = 0
        digiCounter = 0
        for oso,osc in outerShells:
            copyint = ""
            strt = 0 if oso+idxAdder<3 else oso+idxAdder-3
            for j in range(strt,oso+idxAdder):
                if s[j].isdigit(): copyint+=s[j]
            digiCounter = len(copyint)
            copyint = int(copyint)
            
            subDecode = copyint*self.decodeString(s[oso+idxAdder+1:osc+idxAdder])
            s = s[:oso+idxAdder-digiCounter]+subDecode+s[osc+idxAdder+1:]
            idxAdder+=len(subDecode)-osc+oso-1-digiCounter
        return s
