'''
We are given a binary tree (with root node root), a target node, and an integer value k.

Return a list of the values of all nodes that have a distance k from the target node.  The answer can be returned in any order.

 

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2

Output: [7,4,1]

Explanation: 
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.



Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.

'''
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def addParents(node,parent):
            if node:
                node.parent = parent
                addParents(node.left,node)
                addParents(node.right,node)

        addParents(root,None)
        
        memo = [target.val]
        answer = [[target,0]]
        while answer:
            if answer[0][1]==k:
                return [node.val for node,dist in answer]
            node,dist = answer.pop(0)
            for nearestNode in [node.left,node.right,node.parent]:
                if nearestNode and nearestNode.val not in memo:
                    memo.append(nearestNode.val)
                    answer.append([nearestNode,dist+1])
        return []
