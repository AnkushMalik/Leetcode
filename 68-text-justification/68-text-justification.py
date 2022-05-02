class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        s = ''
        for i in words:
            if len(s+i)>maxWidth:
                ans.append(self.justify(s, maxWidth))
                s = i+' '
            elif len(s+i)==maxWidth:
                ans.append(s+i)
                s = ''
            else:
                s+=i+' '
        if len(s)>0: ans.append(self.justify(s, maxWidth, True))
        return ans
    
    def justify(self, s, lim, ljf = False):
        words = s.split(' ')
        tojf = []
        filled = 0
        for i in words:
            if len(i):
                filled+=len(i)
                tojf.append(i)
        spaceToFill = lim-filled
        if len(tojf)==1: return tojf[0]+(' '*spaceToFill)
        if ljf: 
            ans = ' '.join(tojf)
            return ans + ' '*(lim-len(ans))
        lastWord = [tojf[-1]]
        tojf = tojf[:-1]
        while spaceToFill:
            for i in range(len(tojf)):
                if spaceToFill:
                    tojf[i]+=' '
                    spaceToFill-=1
        return ''.join(tojf+lastWord)