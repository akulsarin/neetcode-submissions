# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        node = root
        counter = 0
        last = None

        while stack or node:
            if counter == k:
                break
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                counter += 1
                last = node
                node = node.right

        return last.val
                


        