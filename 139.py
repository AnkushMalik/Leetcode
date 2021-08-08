'''
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        hsh = {}
        def wordBreaker(s,start):
            if start==len(s) or s[start:] in wordDict:
                return True
            if start in hsh:
                return hsh[start]
            for end in range(start+1,len(s)+1):
                if s[start:end] in wordDict and wordBreaker(s,end):
                    hsh[start]=True
                    return hsh[start]
            hsh[start]=False
            return hsh[start]
        return wordBreaker(s,0)
