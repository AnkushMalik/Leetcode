class Solution:
    even = ["00","11","69","88","96"]
    odd = ["0","1","8"]
    def findStrobogrammatic(self, n: int) -> List[str]:
        if n==1:
            return self.odd
        if n==2:
            return self.even[1:]
        
        ans = []
        if n%2==0:
            bases = self.findStrobogrammatic(n-2)
            for i in bases:
                for j in self.even:
                    ans.append(i[:len(i)//2]+j+i[len(i)//2:])
        else:
            bases = self.findStrobogrammatic(n-1)
            for i in bases:
                for j in self.odd:
                    ans.append(i[:len(i)//2]+j+i[len(i)//2:])

        return ans