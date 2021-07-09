'''
Given a character array s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by a single space.

Your code must solve the problem in-place, i.e. without allocating extra space.

 

Example 1:

Input: s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
Example 2:

Input: s = ["a"]
Output: ["a"]
'''
class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s)-1
        spaces = [-1]
        while(i<=j):
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1
        for i in range(len(s)):
            if s[i]==' ':
                spaces.append(i)
        # while()
        while(len(spaces)!=0):
            start = spaces.pop(0)+1
            end = spaces[0]-1 if spaces else len(s)-1
            while(start<=end):
                s[start],s[end]=s[end],s[start]
                start+=1
                end-=1
        return s
