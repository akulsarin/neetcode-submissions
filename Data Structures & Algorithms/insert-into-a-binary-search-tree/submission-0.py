# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        new_node = TreeNode(val=val)
        if not root:
            return new_node

        traverser = root
        inserted = False
        while not inserted:
            if val > traverser.val:
                if traverser.right:
                    traverser = traverser.right
                else:
                    traverser.right = new_node
                    inserted = True
            else:
                if traverser.left:
                    traverser = traverser.left
                else:
                    traverser.left = new_node
                    inserted = True

        return root
                    
        