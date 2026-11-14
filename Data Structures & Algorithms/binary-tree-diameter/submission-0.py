# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """The diameter of the tree is defined as the logest path between any two nodes within the tree. Essentially the height of a nodes left tree + the height of a nodes right sbtree.
        To get the diameter we go to each node of the tree and calculate the heght of its left and right subtrees and add them. This would give us the diameter. each time we get the diamter we store the value in a gloabl variable during the recursion. AT the end we retrun the value.
        This takes O(N) time since we vist each node only once and the dfs will get the height for each node recursively. We need to make diamater non local becasue ints are immuatble so when passing he value in as a function it creates a local shadow not the orignal value"""
        diameter = 0
        def dfs(root):
            nonlocal diameter
            if not root:
                return 0
            
            #get height of left tree
            left = dfs(root.left)
            #get height of the right
            right = dfs(root.right)
            #once we have the height of a nodes left and right we add them to get the dimeter
            diameter = max(diameter,left+right)
            #we add 1 to the max of the left and right to get the height(we tae the max because the tree with the deeper leaf will dicatte the height of the tree)
            return 1 + max(left,right)
        dfs(root)
        return diameter
        
        