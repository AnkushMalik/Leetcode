class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        hp = []

        for i in trips: heappush(hp,(i[1],(i[0],i[2])))
        
        incar = []
        passCount = 0
        while(hp):
            newP = heappop(hp)
            count = newP[1][0]
            i = 0
            while(i<len(incar)):
                pssg = incar[i]
                if pssg[1][1]<=newP[0]:
                    passCount-=pssg[1][0]
                    incar.pop(i)
                    i-=1
                i+=1
            if passCount+count>capacity: return False
            incar.append(newP)
            passCount+=count
        return True