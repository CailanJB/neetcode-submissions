# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """Balanc factor must be 0,1,-1"""
        balanced = True
        def dfs(root):
            nonlocal balanced
            if not root:
                return [True,0]
            
            #get height of left tree
            left = dfs(root.left)
            #get height of the right
            right = dfs(root.right)
            #once we have the height of a nodes left and right we add them to get the dimeter
            if right[1] - left[1] > 1 or right[1] - left[1] < -1:
                balanced = False
                return [balanced,right[1]]
            #we add 1 to the max of the left and right to get the height(we tae the max because the tree with the deeper leaf will dicatte the height of the tree)
            return [balanced, 1 + max(left[1],right[1])]
        return dfs(root)[0]
        
        