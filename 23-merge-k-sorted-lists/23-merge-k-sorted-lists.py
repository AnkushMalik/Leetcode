class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        hp = []
        heapify(hp)
        
        for head in lists:
            while(head):
                heappush(hp,head.val)
                head=head.next
        
        if not hp: return None
        head = ListNode(heappop(hp))
        ans = head
        for _ in range(len(hp)):
            head.next = ListNode(heappop(hp))
            head = head.next
        return ans