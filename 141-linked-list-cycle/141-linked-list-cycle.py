class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if(head == None or head.next==None):
            return False
        slow = head
        fast = head.next
        while fast and fast.next:
            if(slow == fast):
                return True
            slow = slow.next
            fast = fast.next.next
        return False