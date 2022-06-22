class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hp = []
        heapify(hp)
        
        for i in nums:
            heappush(hp,-i)
        
        ans = 0
        for _ in range(k):
            ans = -heappop(hp)
        
        return ans