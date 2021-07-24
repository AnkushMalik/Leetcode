'''
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
'''

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
