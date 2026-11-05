# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """Approach: We run bfs on the tree and after we finsih a level we increment our level count. The number of levels would be equa to the depth of the tree in this proble,. We know we finished a level when the inner loop compltes."""
        if not root: return 0
        
        queue = deque([root])
        level = 0
        while queue:
            length = len(queue)
            for _ in range(length):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level+=1
        return level
        
        