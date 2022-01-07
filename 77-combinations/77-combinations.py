class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.ans = []
        self.findAllComb(list(range(1,n+1)),[],k)
        return self.ans

    def findAllComb(self, arr, carr, lim):
        if len(carr)==lim:
            self.ans.append(carr[:])
        else:
            for i in range(len(arr)):
                carr.append(arr[i])
                self.findAllComb(arr[i+1:],carr,lim)
                carr.pop()