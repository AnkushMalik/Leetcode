class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        j=1
        while j<numRows:
            temp = [1]
            for k in range(1,j):
                temp.insert(k,ans[j-1][k-1]+ans[j-1][k])
            temp.append(1)
            ans.append(temp)
            j+=1
        return ans