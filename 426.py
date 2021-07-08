'''
Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.

You can think of the left and right pointers as synonymous to the predecessor and successor pointers in a doubly-linked list. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

We want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. You should return the pointer to the smallest element of the linked list.

 

Example 1:



Input: root = [4,2,5,1,3]


Output: [1,2,3,4,5]
'''

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return root

        nodeList = self.getInOrder(root)

        for x in range(len(nodeList)):
            nodeList[x].left = nodeList[x-1]
            if x==len(nodeList)-1:
                nodeList[x].right = nodeList[0]
            else:
                nodeList[x].right = nodeList[x+1]
        return nodeList[0]

    def getInOrder(self, root):
        if not root or not root.left and not root.right:
            return [root]
        
        ans = []
        ans += self.getInOrder(root.left) if root.left else []
        ans += [root]
        ans += self.getInOrder(root.right) if root.right else []
        return ans
