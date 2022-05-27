class Solution:
    def myAtoi(self, s: str) -> int:
        signChk = ''
        while len(s) and s[0] in [' ','-','+'] and signChk not in ['-','+']:
            signChk=s[0]
            s=s[1:]
        if s=='': return 0
        
        num = ''
        while len(s) and s[0].isdigit():
            num+=s[0]
            s = s[1:]
        if num=='': return 0
        num = int(num) if signChk!='-' else -int(num)
        if num<-2**31: return -2**31
        elif num>=2**31: return 2**31-1
        else: return num
        