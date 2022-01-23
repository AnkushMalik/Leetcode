class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        s = "123456789"
        ans = []
        for length in range(len(str(low)),len(str(high))+1):
            for i in range(len(s)-length+1):
                num = int(s[i:i+length])
                if num>=low and num<=high: ans.append(num)
        return ans