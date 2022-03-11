# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next: return head
        length = 0
        temp = head
        while(temp):
            length+=1
            temp = temp.next
        k = k%length
        if k==0: return head
        ptr = head
        for i in range(length - k-1):
            ptr = ptr.next
        temp = ptr.next
        ptr.next = None
        ans = temp
        while temp.next:
            temp = temp.next
        temp.next = head
        return ans