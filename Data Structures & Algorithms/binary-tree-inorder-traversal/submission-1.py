# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        current = root

        while current is not None or stack:
            # 1. Traverse as far left as possible, pushing nodes to the stack
            while current is not None:
                stack.append(current)
                current = current.left
            
            # 2. Pop the last node we visited (it has no more left children)
            current = stack.pop()
            
            # 3. Add its value to our result
            result.append(current.val)
            
            # 4. Move to its right child to do the same thing
            current = current.right
            
        return result


            



        