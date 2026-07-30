# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def popMinNodeFromRight(self, root: TreeNode) -> TreeNode:
        prev = root
        curr = root.right
        has_subtree = curr.left is not None
        while curr and curr.left:
            prev = curr
            curr = curr.left

        if has_subtree:
            prev.left = curr.right
        else:
            prev.right = curr.right

        return curr

    def getNodeAndParent(self, dummy: TreeNode, key: int) -> Optional[tuple[TreeNode, TreeNode]]:
        prev = dummy
        traverser = dummy.right
        while True:
            if key == traverser.val:
                return traverser, prev
            elif key > traverser.val and traverser.right:
                prev = traverser
                traverser = traverser.right
            elif key < traverser.val and traverser.left:
                prev = traverser
                traverser = traverser.left
            else:
                return None

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        dummy = TreeNode(val=float('-inf'), right=root)
        traversal_result = self.getNodeAndParent(dummy, key)
        if not traversal_result:
            return root

        node, parent = traversal_result
        if node.val > parent.val:
            if not node.right:
                parent.right = node.left
            elif not node.left:
                parent.right = node.right
            else:
                min_from_right = self.popMinNodeFromRight(node)
                node.val = min_from_right.val
        else:
            if not node.right:
                parent.left = node.left
            elif not node.left:
                parent.left = node.right
            else:
                min_from_right = self.popMinNodeFromRight(node)
                node.val = min_from_right.val

        return dummy.right

        


