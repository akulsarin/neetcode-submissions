# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
            
        nodes = []
        queue = deque([root])
        
        while queue:
            curr = queue.popleft()
            nodes.append(str(curr.val) if curr else "N")
            if curr:
                queue.append(curr.left)
                queue.append(curr.right)
                
        return ",".join(nodes)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        values = [val.strip() for val in data.split(",")]

        root = TreeNode(int(values[0]))
        queue = deque([root])
        
        i = 1
        while queue:
            curr = queue.popleft()
            
            if values[i] != "N":
                curr.left = TreeNode(int(values[i]))
                queue.append(curr.left)
            i += 1
            
            if values[i] != "N":
                curr.right = TreeNode(int(values[i]))
                queue.append(curr.right)
            i += 1
            
        return root




