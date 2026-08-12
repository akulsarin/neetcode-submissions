# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTValidator:
        def __init__(self, isValid: bool, minVal: int | float, maxVal: int | float, count: int):
            self.isValid = isValid
            self.minVal = minVal
            self.maxVal = maxVal
            self.count = count

class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        currMax = 0

        def dfs(node: Optional[TreeNode]) -> BSTValidator:
            nonlocal currMax

            if node is None:
                return BSTValidator(True, float('inf'), float('-inf'), 0)
            
            leftRes = dfs(node.left)
            rightRes = dfs(node.right)

            leftValid = leftRes.isValid and leftRes.maxVal < node.val
            rightValid = rightRes.isValid and rightRes.minVal > node.val

            if leftValid and rightValid:
                currCount = 1 + leftRes.count + rightRes.count
                currMax = max(currMax, currCount)
                return BSTValidator(True, min(node.val, leftRes.minVal), max(node.val, rightRes.maxVal), currCount)

            return BSTValidator(False, float('-inf'), float('inf'), 0)

        dfs(root)
        return currMax
        