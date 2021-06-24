'''Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

Given a balanced string s, split it in the maximum amount of balanced strings.

Return the maximum amount of split balanced strings.

'''


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        bset = {'R':0,'L':0}
        c = 0
        for i in s:
            bset[i]+=1
            if(bset['R']==bset['L']):
                c+=1
                bset['R'] = 0
                bset['L'] = 0
        return c