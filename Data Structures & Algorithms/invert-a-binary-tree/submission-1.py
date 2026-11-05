# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """For every node we need to swap its left and right child.
        after swapping we can recurse on the left tree then recurse on the right tree.
        BFS implementation:
        We use a queue pop fromt he queue swap children and add the new left and right child to the queue if they are not empty"""
        if not root:
            return None
        queue = deque([root])
        while queue:
            node = queue.popleft()
            node.left,node.right = node.right,node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return root

        