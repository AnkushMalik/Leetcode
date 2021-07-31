'''
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

 

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
'''
class Solution:
    bitData = {0:'0'}
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            bitn = self.getBit(i)
            self.bitData[i]=bitn
            c = 0
            for j in bitn:
                if j=='1': c+=1
            ans.insert(i,c)
        return ans
    
    def getBit(self,n):
        if n in self.bitData: 
            return self.bitData[n]
        return self.incBit(self.getBit(n-1))
    
    def incBit(self,n):
        carr = True
        i = len(n)-1
        n = list(n)
        while carr and i>=0:
            if n[i]=='0':
                n[i]='1'
                carr=False
            else:
                n[i]='0'
                i-=1
        if carr: n.insert(0,'1')
        return ''.join(n)

#after learning bit manipulation trick in Q.191
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            ans.insert(i,self.popCount(i))
        return ans
    
    def popCount(self,n):
        s = 0
        while n!=0:
            n &=(n-1)
            s+=1
        return s