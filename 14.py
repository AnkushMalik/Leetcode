'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 
'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if(len(strs)==1):
            return strs[0]
        k = strs[0]

        for i in range(len(k)):
            c = 1
            for m in strs[1:]:
                if(i<len(m) and m[i]==k[i]):
                    c+=1
            if c!=len(strs):
                return k[:i]
                
        return k