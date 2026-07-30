# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def buildTreeRecursive(preorder_lst: List[int], inorder_lst: List[int]) -> Optional[TreeNode]:
            inorder_indices = {val: idx for idx, val in enumerate(inorder_lst)}
            preorder_indices = {val: idx for idx, val in enumerate(preorder_lst)}
            # print(preorder_lst)
            # print(inorder_lst)
            # print("\n")
            if not preorder_lst:
                return None

            root = TreeNode(val=preorder_lst[0])
            if len(preorder_lst) == 1:
                return root

            pivot_idx = inorder_indices[root.val]

            left_inorder = inorder_lst[:pivot_idx]
            right_inorder = inorder_lst[pivot_idx + 1:]

            left_preorder = []
            right_preorder = []

            for val in preorder_lst[1:]:
                if inorder_indices[val] < pivot_idx:
                    left_preorder.append(val)
                elif inorder_indices[val] > pivot_idx:
                    right_preorder.append(val)

            root.left = buildTreeRecursive(left_preorder, left_inorder)
            root.right = buildTreeRecursive(right_preorder, right_inorder)

            return root

        return buildTreeRecursive(preorder, inorder)
            







                    