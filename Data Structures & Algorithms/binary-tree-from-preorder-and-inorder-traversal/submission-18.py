# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        N = len(preorder)
        inorderIndices = {val: idx for idx, val in enumerate(inorder)}
        preorderIdx = 0

        def construct(l: int, r: int) -> Optional[TreeNode]:
            nonlocal preorderIdx
            if preorderIdx >= N or r - l < 0:
                return None

            root = TreeNode(preorder[preorderIdx])
            preorderIdx += 1
            
            inorderIdx = inorderIndices[root.val]
            
            root.left = construct(l, inorderIdx - 1)
            root.right = construct(inorderIdx + 1, r)

            return root

        root = construct(0, N - 1)
        return root