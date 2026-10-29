class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def dfs(node):
            if not node:
                return
            result.append(node.val)  # Visit root
            dfs(node.left)           # Traverse left
            dfs(node.right)          # Traverse right
            
        dfs(root)
        return result