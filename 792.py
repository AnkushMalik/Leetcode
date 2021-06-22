'''
Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
 

Example 1:

Input: s = "abcde", words = ["a","bb","acd","ace"]
Output: 3
Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".
'''

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        count = 0
        setS = set(s)
        for word in words:
            i = 0
            j = len(s)-1
            if(set(word).issubset(setS)):
                while(j>=i and len(word)!=0):
                    if(word[0]==s[i]):
                        word = word[1:]
                    if(len(word)!=0 and word[-1]==s[j]):
                        word=word[:-1]
                    i+=1
                    j-=1
            if(len(word)==0):
                count+=1
        return count
