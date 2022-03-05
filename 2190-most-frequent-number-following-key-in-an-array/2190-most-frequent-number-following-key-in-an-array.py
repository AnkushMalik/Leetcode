class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        hsh = {}
        for i in range(len(nums)-1):
            if nums[i]==key:
                target = nums[i+1]
                if target in hsh:
                    hsh[target]+=1
                else: hsh[target]=1
        ans = [0,0];
        for i in hsh:
            if hsh[i]>ans[1]:
                ans = [i,hsh[i]]
        return ans[0]