class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        hsh = {}
        for i in time:
            rem = i%60
            if rem in hsh:
                hsh[rem]+=1
            else:
                hsh[rem]=1
        count = 0
        for i in range(1,30):
            if i in hsh and 60-i in hsh:
                count+= (hsh[i]*hsh[60-i])
        if 0 in hsh:
            count+=(hsh[0]*(hsh[0]-1))//2
        if 30 in hsh:
            count+=(hsh[30]*(hsh[30]-1))//2
        return count
                