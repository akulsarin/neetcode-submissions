# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        stack = []
        node = root
        depths = {None: 0}
        last = None

        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack[-1]
                if not node.right or node.right in depths:
                    stack.pop()
                    
                    left_height = depths[node.left]
                    right_height = depths[node.right]

                    if abs(left_height - right_height) > 1:
                        return False
                    
                    depths[node] = 1 + max(left_height, right_height)
                    last = node
                    node = None
                else:
                    node = node.right

        return True






        
        
        