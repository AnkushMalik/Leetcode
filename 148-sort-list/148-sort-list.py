# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        vals = []
        ptr = head
        while ptr:
            vals.append(ptr.val)
            ptr = ptr.next
        ptr2 = head
        i = 0
        vals.sort()
        while ptr2:
            ptr2.val = vals[i]
            ptr2 = ptr2.next
            i+=1
        return head